import pandas as pd
import pandera.pandas as pa
from pandera import Check
import sys


class AdvancedStudentAnalytics:
    def __init__(self, df):
        self.df = df
        self._prepare_data()
        try:
            self._validate_df()
        except Exception as e:
            print(e)
            sys.exit('Ошибка данных')
    def _prepare_data(self):
        ratings_df = self.df.loc[:, ['math', 'physics', 'cs']]
        self.df["average_grade"] = ratings_df.mean(axis=1)
        self.df["project_score"] = self.df["project_score"].fillna("Unknown")

        self.df.loc[self.df['average_grade'] >= 85, 'performance_level'] = 'high'
        self.df.loc[(self.df['average_grade'] <= 84) & (self.df['average_grade'] <= 84), 'performance_level'] = 'medium'
        self.df.loc[self.df['average_grade'] < 70, 'performance_level'] = 'low'

        self.df["risk_level"] = "low risk"
        self.df.loc[(self.df['attendance'] < 60) | (self.df['average_grade'] < 65), 'risk_level'] = 'high risk'
        self.df.loc[(self.df['attendance'] >= 60) & (self.df['attendance'] <= 65), 'risk_level'] = 'medium risk'

    def _validate_df(self):
        schema = pa.DataFrameSchema({
            'name': pa.Column(str),
            'group': pa.Column(str, checks=Check.isin(['A1', 'A2', 'B1', 'B2', 'C1'])),
            'math': pa.Column(int, checks=Check.in_range(0, 101)),
            'physics': pa.Column(int, checks=Check.in_range(0, 101)),
            'cs': pa.Column(int, checks=Check.in_range(0, 101)),
            'attendance': pa.Column(int, checks=Check.in_range(0, 101)),
            'city': pa.Column(str),
            'enrollment_year': pa.Column(int),
            'scholarship': pa.Column(bool),
            "project_score": pa.Column(
                object,
                checks=Check(lambda s: s.apply(lambda x: x == "Unknown" or isinstance(x, (int, float))))
            )
        })
        return schema.validate(self.df)

    def recommends(self):
        students_at_risk_groped = self.at_risk_students().groupby('group').agg(
            count=("risk_level", "count")
        )

        for index, value in students_at_risk_groped['count'].items():
            if value > 6:
                yield index

        # Дальше придумывать слегка лень

    def top_students(self, n):
        df_sorted = self.df.sort_values('average_grade', ascending= False)
        return df_sorted.iloc[:n]

    def group_stats(self):
        grouped_df = self.df.groupby('group').agg(
            average_grade=('average_grade', 'mean'),
            mean_attendance=('attendance', 'mean'),
        )
        grouped_df['size'] = self.df.groupby('group').size()
        return grouped_df

    def at_risk_students(self):
        return self.df.loc[self.df['risk_level'] == 'high risk']

    def scholarship_analysis(self):
        with_scholarship_df = self.df.loc[self.df['scholarship'] == True]
        without_scholarship_df = self.df.loc[self.df['scholarship'] == False]
        return with_scholarship_df.shape[0], without_scholarship_df.shape[0]

    def city_performance(self):
        city_df = self.df.groupby('city').agg(
            average_grade=('average_grade', 'mean'),
        )
        top_city = city_df[city_df['average_grade'] == city_df['average_grade'].max()]
        worst_city = city_df[city_df['average_grade'] == city_df['average_grade'].min()]

        return pd.concat([top_city, worst_city]).to_dict()['average_grade']


    def hidden_top_students(self):
        return self.df.loc[(self.df['average_grade'] > 85) & (self.df['scholarship'] == False)]

    def lazy_geniuses(self):
        return self.df.loc[(self.df['average_grade'] > 85) & (self.df['attendance'] < 60)]

    def performance_distribution(self):
        percentages = self.df["performance_level"].value_counts(normalize=True) * 100

        return percentages

    def full_analysis(self):
        top_3 = list(self.top_students(3)['name'])
        group_stats = self.group_stats()
        scholarship_analysis = f'Со стипендией: {self.scholarship_analysis()[0]} , без: {self.scholarship_analysis()[1]}'
        risk_count = len(self.at_risk_students())
        hidden_top_count = len(self.hidden_top_students())
        lazy_geniuses_count = len(self.lazy_geniuses())

        return_dict = {
            'top_3': top_3,
            'group_stats': group_stats,
            'scholarship_analysis': scholarship_analysis,
            'risk_count': risk_count,
            'hidden_top_count': hidden_top_count,
            'lazy_geniuses_count': lazy_geniuses_count,
        }

        return return_dict


pd.set_option('display.max_rows', None)

analytics = AdvancedStudentAnalytics(pd.read_csv('students_extended.csv'))
# print(analytics.top_students(3))
# print(analytics.group_stats())
# print(analytics.full_analysis())
# print(analytics.df["project_score"])
# print(analytics.performance_distribution())

for i in analytics.recommends():
    print(f"В группе {i} слишком много студентов в зоне риска")
