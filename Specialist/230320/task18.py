class Reactangle:
    A = 0.0
    B = 0.0
def perimetr(r : Reactangle) -> float:
    return (r.A + r.B) * 2
def area(r : Reactangle) -> float:
    return r.A * r.B
c = Circle()
c.R = 1
print(perimetr(c))