# class Point:
    # X = 0
    # Y = 0
    # def setup(self, X_set, Y_set):
        # self.X = X_set
        # self.Y = Y_set
# p1 = Point()
# p1.setup(10, 200)

# p2 = Point()

# print(p1.X, p1.Y)
# print(p2.X, p2.Y)


class Point:
    def __init__(self, X_set = 0, Y_set = 0):
        print('Construct works')
        self.X = X_set
        self.Y = Y_set
p1 = Point(10, 200)
p2 = Point()
# p2 = Point()
print(p1.X, p1.Y)
print(p2.X, p2.Y)

def on_line_with(self, p1, p2) -> bool:
        return (p2.X * (p1.Y - self.Y) - p2.Y * (p1.X - self.X) == self.X * p1.Y - p1.X * self.Y)
