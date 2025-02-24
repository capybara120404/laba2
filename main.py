def main():
    print("Добро пожаловать в калькулятор стоимости покраски автомобиля!")
    detail, color = get_user_input()
    cost = calculate_cost(detail, color)
    print(f"Стоимость покраски детали '{detail}' в цвет '{color}': {cost:.2f} рублей")

    detail = input("Введите деталь: ").lower()
    while detail not in details:
        detail = input("Неверная деталь. Введите ещё раз: ").lower()

    color = input("Введите цвет: ").lower()
    while color not in colors:
        color = input("Неверный цвет. Введите ещё раз: ").lower()

    return detail, color

if name == "main":
    main()

