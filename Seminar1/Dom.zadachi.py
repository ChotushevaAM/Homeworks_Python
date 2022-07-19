# Zadacha 1

# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*

# 6 -> да
# 7 -> да
# 1 -> нет

# print('Введите номер дня недели')
# number = int(input())
# if number < 6:
#     print('Net')
# elif number == 6:
#     print('Da')
# elif number == 7:
#     print('Da')


# Zadacha 2

# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  """


# def inputNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Введите значение {xyz[i]}: "))
#     return a


# def checkPredicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left == right
#     return result


# statement = inputNumbers(3)

# if checkPredicate(statement) == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")


# Zadacha 4

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#     print('Первая четверть')
# elif x > 0 and y < 0:
#     print('Четвертая четверть')
# elif x < 0 and y > 0:
#     print('Вторая четверть')
# elif x < 0 and y < 0:
#     print('Третья четверть')
# else:
#     print('Начало координат')


# Zadacha 5

# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве. 
# Пример: - A (3,6); B (2,1) -> 5,09 - A (7,-5); B (1,-1) -> 7,21 


def inputNumbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        coordinate = False
        while not coordinate:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                coordinate = True
            except ValueError:
                print("Ты ошибся. Вводить надо целые числа!")
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Введите координаты точки А")
pointA = inputNumbers(2)
print("Введите координаты точки В")
pointB = inputNumbers(2)

print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")