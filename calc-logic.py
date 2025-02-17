details_coef = {
    "капот": 1.0,
    "передняя дверь": 1.2,
    "задняя дверь": 1.1,
    "передний бампер": 1.0,
    "задний бампер": 1.0,
    "крыша": 1.1
}

colors_coef = {
    "белый": 1.0,
    "синий": 1.0,
    "желтый": 1.1,
    "красный": 1.0,
    "перламутровый": 1.2,
    "серый металлик": 1.3
}

def calculate_cost(detail, color):
    base_cost = 12000
    return base_cost * details_coef.get(detail, 1) * colors_coef.get(color, 1)