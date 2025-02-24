def get_user_input():
    details = ["капот", "передняя дверь", "задняя дверь", "передний бампер", "задний бампер", "крыша"]
    colors = ["белый", "синий", "желтый", "красный", "перламутровый", "серый металлик"]

    detail = input("Введите деталь: ").lower()
    while detail not in details:
        detail = input("Неверная деталь. Введите ещё раз: ").lower()

    color = input("Введите цвет: ").lower()
    while color not in colors:
        color = input("Неверный цвет. Введите ещё раз: ").lower()

    return detail, color
def main():
    print("Добро пожаловать в калькулятор стоимости покраски автомобиля!")
    detail, color = get_user_input()
    cost = calculate_cost(detail, color)
    print(f"Стоимость покраски детали '{detail}' в цвет '{color}': {cost:.2f} рублей")

if name == "main":
    main()
