import matplotlib.pyplot as plt


def visual_show(points):
    # Extract x and y coordinates from list
    x_coord = [coord[0] for coord in points]
    y_coord = [coord[1] for coord in points]
    plt.plot(x_coord, y_coord, marker="o", color="red")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()


def create_all_points(octave_points):
    points = []  # List to store all the points
    for point in octave_points:
        x, y = point
        points.append((x, y))  # one
    for point in octave_points:
        x, y = point
        points.append((y, x))  # two
    for point in octave_points:
        x, y = point
        points.append((-y, x))  # three
    for point in octave_points:
        x, y = point
        points.append((-x, y))  # four
    for point in octave_points:
        x, y = point
        points.append((-x, -y))  # five
    for point in octave_points:
        x, y = point
        points.append((-y, -x))  # six
    for point in octave_points:
        x, y = point
        points.append((y, -x))  # seven
    for point in octave_points:
        x, y = point
        points.append((x, -y))   # eight

    print(points)
    visual_show(points)


def bresenham_circle(radius):
    # print(radius)
    octave_points = []
    octave_d = []
    x, y = 0, radius
    # print(f'x, y: {x, y}')
    # Best case for Decision Parameter
    d = 3 - (2*radius)
    while x <= y:
        octave_points.append((x, y))
        octave_d.append(d)
        x += 1
        if d > 0:
            d = d + 4*(x - y) + 10
            y -= 1
        else:
            d = d + 4*x + 6
    print(octave_d)
    create_all_points(octave_points)


def main():
    print("\nBresenham's Circle Drawing Algorithm")
    # Base coordinate pair of the circle center
    center = [0, 0]
    # # Input Center of the Circle
    # x = int(input('Enter x coordinate of the center: '))
    # y = int(input('Enter y coordinate of the center: '))
    # center = [x, y]
    print(f'Center of circle as {center}')

    # Test Purpose
    # radius = 10

    # Taking input from user for radius
    radius = int(input('Enter the radius of the circle: '))
    # print(radius)
    bresenham_circle(radius)


if __name__ == "__main__":
    main()
