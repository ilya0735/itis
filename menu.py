menu = {
    "coffee": 120,
    "tea": 80,
    "sandwich": 200,
    "cake": 150,
    "juice": 100
}


def show_menu():
    print("==================================================================")
    list_of_menu = list(menu.items())
    print("Меню отсортированное по алфавиту:")
    alphabet_sorted_menu = sorted(list_of_menu)
    for dish, price in alphabet_sorted_menu:
        print(f"{dish} : {price}")
    print()
    print("Меню отсортированное по цене:")
    price_sorted_menu = sorted(list_of_menu, key=lambda x: x[1])
    for dish, price in price_sorted_menu:
        print(f"{dish} : {price}")
    print("==================================================================")


def average_price():
    list_of_menu = list(menu.items())
    list_of_dishes, list_of_prices = zip(*list_of_menu)
    average_price = sum(list_of_prices) / len(list_of_prices)
    print(f"Средняя цена меню: {average_price}")


def update_menu():
    try:
        new_dish = input("Введите новое блюдо:")
        new_dish = new_dish.lower()
        price_for_new_dish = int(input("Введите цену для новго блюда:"))
        update_menu = {new_dish:price_for_new_dish}
        menu.update(update_menu)
        print("Блюдо успешно добавлено в меню!")
    except ValueError:
        print("Цена должна быть числом")


def delete_dish():
    dish = input("Введите блюдо которое хотите удалить:")
    dish = dish.lower()
    menu.pop(dish) if dish in menu else print("Такого блюда нет в меню")


def menu_cheeper_when_N():
    N = int(input("Выберите значение:"))
    list_of_menu = list(menu.items())
    list_of_dishes, list_of_prices = zip(*list_of_menu)
    list_of_prices = list(list_of_prices)
    list_cheeper_when_N = list(filter(lambda x: x < N, list_of_prices))
    list_of_dishes = []
    print("==================================================================")
    print("Список блюд дешевле выбраного значения:")
    for key, value in menu.items():
        if value in list_cheeper_when_N:
            list_of_dishes.append(key)
    print(list_of_dishes)
    print("==================================================================")


def max_min_menu_position():
    list_of_menu = list(menu.items())
    max_position = max(list_of_menu, key=lambda x: x[1])
    min_position = min(list_of_menu, key=lambda x: x[1])
    print("==================================================================")
    print(f"Самое дорогое блюдо {max_position[0]} : {max_position[1]}")
    print(f"Самое дешевое блюдо {min_position[0]} : {min_position[1]}")
    print("==================================================================")
    

def menu_of_drinks():
    list_of_menu = list(menu.items())
    price_sorted_menu = sorted(list_of_menu, key=lambda x: x[1])
    first_3_position = list(filter(lambda x: x[1] < 150, price_sorted_menu))
    print("==================================================================")
    print("Список напитков:")
    for dish, price in first_3_position:
        print(f"{dish} : {price}")
    print("==================================================================")


def make_order():
    try: 
        from functools import reduce
        # 9
        order_dict = {}
        order = input("Введите ваш заказ (через запятую):")
        list_of_dishes, list_of_prices = zip(*menu.items())
        order_without_space = order.replace(" ", "")
        order_without_space = order_without_space.lower()
        order_list = order_without_space.split(",")
        # 12
        flag_for_12 = [True]
        if len(order) == 0:
            flag_for_12 = [False]
        if all(flag_for_12) == False:
            print()
            print("Вы ничего не выбрали")

        true_order = list(filter(lambda x: x in list_of_dishes, order_list))
        list_of_order_prices = []
        for dish, price in menu.items():
            if dish in true_order:
                order_dict[dish] = price
                list_of_order_prices.append(price)
        
        # 10
        sum_of_order = reduce(lambda a, b: a + b, list_of_order_prices)
        
        # 11
        print("==================================================================")
        print("Ваш заказ:")
        for i, (dish, price) in enumerate(order_dict.items(), start=1):
            print(f"{i}. {dish} - {price} руб.")


        print(f"Итого: {sum_of_order} руб.")
        print("==================================================================")

        if sum_of_order > 500:
            print("Поздравляем, у вас скидка 10%!")
            print()
    except TypeError:
        print()



    

print("1. Показать меню",
    "2. Вывести среднюю цену блюд",
    "3. Обновить меню",
    "4. Удалить блюдо из меню",
    "5. Список блюд дешевле выбраного значения",
    "6. Самое дорогое и дешевое блюдо в меню",
    "7. Вывести мписок напитков отсортированный по цене",
    "8. Сделать заказ",
    "9. Выход из программы", sep="\n")

while True:
    choic = input("Введите команду:")
    if choic == "1":
        show_menu()
    elif choic == "2":
        average_price()
    elif choic == "3":
        update_menu()
    elif choic == "4":
        delete_dish()
    elif choic == "5":
        menu_cheeper_when_N()
    elif choic == "6":
        max_min_menu_position()
    elif choic == "7":
        menu_of_drinks()
    elif choic == "8":
        make_order()
    elif choic == "9":
        break
    else:
        print("Введите корректную команду")



