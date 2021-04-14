class Point:
    def __init__(self, X_set : int = 0, Y_set : int = 0):
        print('Construct works')
        self.X = X_set
        self.Y = Y_set
    def on_line_with(self, p1, p2) -> bool:
        k = (p1.Y - p2.Y) / (p1.X - p2.X)
        b = p2.Y - k * p2.X
        return self.Y == k * self.X + b
p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = Point(3, 3)
# p1
print(p1.on_line_with(p2, p3))