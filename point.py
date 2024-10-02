
import math


class Point:

    x = 0
    y = 0

    # def __init__(self):
    #     self.reset()
        

    def move(self, x: float, y: float):
        self.x = x
        self.y = y
        return self.x, self.y

    def reset(self):
        return 0.0, 0.0

    def calc_distance(self, other: 'Point'):
        # return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return math.hypot(self.x - other.x, self.y - other.y)


if __name__ == "__main__":
    p1 = Point()
    p2 = Point()

    p1.reset()
    p2.reset()

    print(p1.x, p1.y)
    print(p2.x, p2.y)

    p1.move(4, 7)
    p2.move(6, 2)

    print("After moving")
    print(p1.x, p1.y)
    print(p2.x, p2.y)

    print("find difference")
    print(p1.calc_distance(p2))
