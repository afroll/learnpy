A,B,C = int(input()), int(input()), int(input())
if A == 0:
    if B == 0:
        print()
    else:
        print('x: %.2f'%(-C/B))
else:
    D = B**2 - 4*A*C
    if D > 0:
        x1 = (-B + D ** 0.5) / (2 * A)
        x2 = (-B - D ** 0.5) / (2 * A)
        print('x1: %.2f'%(x1))
        print('x2:  %.2f'%(x2))
    elif D == 0:
         x1 = -B / (2 * A)
# print('x: '(x))