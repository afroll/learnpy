# def fibonacci(n):
#      if n in (1, 2):
#          return 1
#      return fibonacci(n - 1) + fibonacci(n - 2)
# fibonacci = int(input())
# print(a = [n for n in a if not n%2])
# n = int(input())
# f1 = 1
# f2 = 2
# print(f1, f2, end=" ")
# for i in range(3,n+1):4
#     print(f1 + f2, end=" ")
#     b = f1
#     f1 = f2
#     f2 = b+f1
# print()

# def fib():
#     a, b = 1, 1
#     yield a
#     while True:
#         yield b
#         a, b = b, a + b

# def even_fib(n=10000):
#     for i in fib():
#         if i > n:
#             return
#         if i % 2 == 0:
#             yield i

#
# def fib(n):
#     f1 = 0
#     f2 = 1
#     k = 1
#     a = [0]
#     while n != k:
#         f3 = f1 + f2
#         f1 = f2
#         f2 = f3
#         if f3 % 2 == 0: # проверка чётное или нет.
#             a.append(f3)
#             k += 1
#     for i in a:
#         print(i, end = ' ')
# fib(int(input()))

def fib(n):
    f1 = 0 # первый элемент последовательности Фибоначчи
    f2 = 1 # второй элемент последовательности Фибоначчи
    a = [0]
    while n != len(a):
        f3 = f1 + f2 # находим третий элемент последовательности Фибоначчи
        f1 = f2 # cохраняем второй элемент в переменную
        f2 = f3 # сохраняем третий элемент в переменную
        if f3 % 2 == 0: # проверка чётное ли число
            a.append(f3)
    for i in a: # выводим все чётные числа
        print(i, end = ' ') # используем чтобы вывести в одну строку
fib(int(input()))