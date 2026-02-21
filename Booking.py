class Bomzh(Exception):
    pass


class Booking:
    def __init__(self, user_name, user_age, ticket_count, budget):
        self.name = user_name
        self.age = user_age
        self.ticket_count = ticket_count
        self.budget = budget

    def validate_name(self):
        if self.name == "":
            raise ValueError("Имя не может быть пустым")

    def validate_age(self):
        if not(self.age.isdigit()):
            raise ValueError("Возраст должен быть числом")
        if int(self.age) < 12:
            raise ValueError("Слишком маленький возраст")

    def validate_tickets(self):
        if (not(self.ticket_count.isdigit())) or (int(self.ticket_count) <= 0) or (int(self.ticket_count) > 5):
            raise ValueError("Некорректное количество билетов")

    def validate_budget(self):
        if (not(self.budget.isdigit())) or (int(self.budget) < 0):
            raise ValueError("Некорректный бюджет")

    def validate_order(self):
        if int(self.ticket_count) * 500 > int(self.budget):
            raise Bomzh("Вы слишком бедны для таких покупок")

    def validate_check(self):
        self.validate_name()
        self.validate_age()
        self.validate_tickets()
        self.validate_budget()
        self.validate_order()

    def calculate(self):
        self.validate_check()
        return int(self.ticket_count) * 500, int(self.budget) - int(self.ticket_count) * 500


name = "Илья"
age = "18"
tickets_count = "2"
budget = "10000"

try:
    order = Booking(name, age, tickets_count, budget)
    print(order.calculate())
except Exception as e:
    print(e)
    print("Регистрация не прошла")

