def main():
    print("Добро пожаловать в калькулятор стоимости покраски автомобиля!")
    detail, color = get_user_input()
    cost = calculate_cost(detail, color)
    print(f"Стоимость покраски детали '{detail}' в цвет '{color}': {cost:.2f} рублей")

if name == "main":
    main()