# print('Решаем уравнение a•x²+b•x+c=0')
A = float(input())
B = float(input())
C = float(input())
D = B ** 2 - 4 * A * C
print('Дискриминант = ' + str(D))
if D < 0:
    print()
elif D == 0:
    x = -B / (2 * A)
    print('x = ' + str(x))
else:
    x1 = (-B + D ** 0.5) / (2 * A)
    x2 = (-B - D ** 0.5) / (2 * A)
    print('x1: %.2f'% + (x1))
    print('x2:  %.2f'% + (x2))