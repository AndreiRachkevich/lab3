# Рекурсивное вычисление чисел  ряда Фибоначчи

n = int(input("Введите число членов последовательности:"))
def fibonacci(n):
    f = 1
    if (n > 2):
        f = (fibonacci(n-1) + fibonacci(n-2))
    return f
print("Последовательность чисел ряда Фибоначчи:")
for i in range(n):
    print(fibonacci(i))