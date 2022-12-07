import math
import matplotlib.pyplot as plt
import random


# point object
class Point:
    def __init__(self, point_x, point_y):
        self.x = point_x
        self.y = point_y


# draw empty plot
def draw_plot():
    fig = plt.figure()
    aux_plot = fig.add_subplot(111)
    aux_plot.set_xlabel('x-points')
    aux_plot.set_ylabel('y-points')
    aux_plot.set_title('Sierpinsky Triangle')
    return aux_plot


# generate random point in triangle
def get_random_point_in_triangle(point_a, point_b, point_c):
    p1 = random.uniform(0.0, 1.0)
    p2 = random.uniform(0.0, 1.0)
    px = (1 - math.sqrt(p1)) * point_a.x + (math.sqrt(p1) * (1 - p2)) * point_b.x + (math.sqrt(p1) * p2) * point_c.x

    p1 = random.uniform(0.0, 1.0)
    p2 = random.uniform(0.0, 1.0)
    py = (1 - math.sqrt(p1)) * point_a.y + (math.sqrt(p1) * (1 - p2)) * point_b.y + (math.sqrt(p1) * p2) * point_c.y

    return Point(px, py)


if __name__ == '__main__':
    plot = draw_plot()

    # triangle definition
    a = Point(0, 0)
    b = Point(100, 0)
    c = Point(50, 100)
    triangle = [a, b, c]

    # start point, can be fixed or random
    # start = Point(x, y)
    start = get_random_point_in_triangle(a, b, c)

    # number of points to draw
    iterations = 5000

    # draw points
    plot.scatter(a.x, a.y, s=1)
    plot.scatter(b.x, b.y, s=1)
    plot.scatter(c.x, c.y, s=1)
    plot.scatter(start.x, start.y, s=1)

    last = start
    for x in range(iterations):
        p_origin = random.choice(triangle)
        average_point = Point((p_origin.x + last.x) / 2, (p_origin.y + last.y) / 2)
        plot.scatter(average_point.x, average_point.y, s=1)
        last = average_point

    # show plot
    plt.show()
