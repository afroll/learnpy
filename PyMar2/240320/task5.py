A = float(input())
B = float(input())
C = float(input())
D = B ** 2 - 4 * A * C
if D < 0:
    print()
elif D == 0:
    x1 = -B / (2 * A)
    print('x1: '+ str(x1))
else:
    x1 = (-B + D ** 0.5) / (2 * A)
    x2 = (-B - D ** 0.5) / (2 * A)
    print('x1: %.2f'%(x1))
    print('x2:  %.2f'%(x2))