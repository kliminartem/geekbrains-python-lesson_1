__author__ = 'Климин Артем Владимирович'

# Задача 1

print("Задача 1")
userNumber = input("Введите число ")
for eachItem in range(len(userNumber)):
    print(userNumber[eachItem])
print("Задача 1 завершена")

# Задача 2

print("Задача 2")
a = input("Ведите значение переменной a ")
b = input("Ведите значение переменной b ")
a, b = b, a
print("Теперь переменная a = " + a)
print("Теперь переменная b = " + b)
print("Задача 2 завершена")

# Задача 3

print("Задача 3")
userAge = int(input("Ведите ваш возраст "))
if userAge >= 18:
    print("Извините, пользование данным ресурсом только с 18 лет")
else:
    print("Доступ разрешен")
print("Задача 3 завершена")
