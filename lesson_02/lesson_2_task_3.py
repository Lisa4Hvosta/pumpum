import math


def square(side):
    area = side * side
    return math.ceil(area)


user_input = input("Введите сторону: ")
side = float(user_input)
result = square(side)

print(f"Площадь квадрата: {result}")
