class Circle:
    R = 0
class Reactangle:
    A = 0.0
    B = 0.0
def Ratio(c : Circle, r:Reactangle) -> bool:
    answer = (c.R *2 <= r.A and c.R * 2 <= r.B)
    return answer
c = Circle()
c.R = 20
r = Reactangle()
r.A, r.B = 100, 200
print(Ratio(c,r))