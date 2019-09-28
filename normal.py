import math

__author__ = 'Климин Артем Владимирович'

# Задача 1

print("Задача 1: вывести максимальное число из введенных пользователем")
userNumber = input("Введите число ")
biggerNumber = 0
for eachItem in range(len(userNumber)):
    thisNumber = int(userNumber[eachItem])
    if biggerNumber < thisNumber:
        biggerNumber = thisNumber
print(biggerNumber)
print("Задача 1 завершена ")

# Задача 2

print("Задача 2: поменять значения переменных местами")
a = input("Ведите значение переменной a ")
b = input("Ведите значение переменной b ")
a, b = b, a
print("Теперь переменная a = " + a)
print("Теперь переменная b = " + b)
print("Задача 2 завершена ")

# Задача 3

print("Задача 3: получить корень квадратного уравнения типа ax² + bx + c = 0")
a = int(input("Ведите значение коэфицента a (кроме 0) "))
b = int(input("Ведите значение коэфицента b "))
c = int(input("Ведите значение коэфицента c "))
D = b * b - 4 * a * c
if D == 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    print(x1)
elif D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("Первый корень = " + str(x1))
    print("Второй корень = " + str(x2))
else:
    print("Корней нет");
print("Задача 3 завершена ")
