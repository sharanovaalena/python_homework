import math


def square(old_square):
    return math.ceil(old_square * old_square)


old_square = float(input("чему равна сторона квадрата? "))
print(f"Площадь квадрата равна {square(old_square)}")
