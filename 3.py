# Задача на рекурсию
#
# Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b на квадраты с наибольшей возможной
# на каждом этапе стороной. Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.
a = int(input('Введите высоту'))
b = int(input('Введите ширину'))
n = 0
def square(a, b, n):
    if a == b:
        print('Длины ребер получаемых квадратов:', a)
        return n + 1
    elif a > b:
       return square(a - b, b, n + 1)
       print('Длины ребер получаемых квадратов:', b)
    elif a < b:
        return square(a, b - a, n + 1)
        print('Длины ребер получаемых квадратов:', a)

print('Кол-во квадратов:',square(a, b, n))
