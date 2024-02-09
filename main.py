import matplotlib.pyplot as plt


def visual_show(all_points, point1, point2):
    # Extract x and y coordinates from list
    x_coord = [coord[0] for coord in all_points]
    y_coord = [coord[1] for coord in all_points]
    plt.plot(x_coord, y_coord, marker='o', color='red')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Bresenham's Algorithm: Visuals")
    plt.grid(True)
    x = [point1[0], point2[0]]
    y = [point1[1], point2[1]]
    plt.plot(x, y, marker='o', color='blue')
    plt.show()


def slope_less_than_one(point1, point2):
    print('Points are: ', point1, point2)
    print('Slope is lesser than one')
    all_points = []
    all_p = []
    x1, y1 = point1
    x2, y2 = point2
    x, y = x1, y1
    dy = y2 - y1
    dx = x2 - x1
    p = 2 * dy - dx

    while x <= x2:
        all_points.append((x, y))
        all_p.append(p)
        x += 1
        if p < 0:
            p = p + 2 * dy
        else:
            p = p + 2 * dy - 2 * dx
            y += 1
    print("Intermediate Points are: ", all_points)
    print("Decision Parameters are: ", all_p)
    visual_show(all_points, point1, point2)


def slope_greater_than_one(point1, point2):
    print('Points are: ', point1, point2)
    print('Slope is greater or equal one')
    all_points = []
    all_p = []
    x1, y1 = point1
    x2, y2 = point2
    x, y = x1, y1
    dy = y2 - y1
    dx = x2 - x1
    p = 2 * dx - dy

    while y <= y2:
        all_points.append((x, y))
        all_p.append(p)
        y += 1
        if p < 0:
            p = p + 2 * dx
        else:
            p = p + 2 * dx - 2 * dy
            x += 1
    print("Intermediate Points are: ", all_points)
    print("Decision Parameters are: ", all_p)
    visual_show(all_points, point1, point2)


def bresenham_line(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dy = y2 - y1
    dx = x2 - x1
    if dy < dx:
        slope_less_than_one(point1, point2)
    else:
        slope_greater_than_one(point1, point2)


def inputCoordinates(i):
    print('Case: ', i + 1)
    print('Input the First Coordinate:')
    x1 = int(input('Enter the X1: '))
    y1 = int(input('Enter the Y1: '))
    print('Input the Second Coordinate: ')
    x2 = int(input('Enter the X2: '))
    y2 = int(input('Enter the Y2: '))
    point1 = [x1, y1]
    point2 = [x2, y2]
    bresenham_line(point1, point2)


def main():
    print('\nBresenham Line Drawing Algorithm')
    # Test Purpose
    point1 = [1, 1]
    point2 = [8, 4]
    bresenham_line(point1, point2)

    point1 = [1, 1]
    point2 = [4, 8]
    bresenham_line(point1, point2)
    # Actual Data
    # n = int(input('How many cases do you have?: '))
    # for i in range(n):
    #     inputCoordinates(i)


if __name__ == "__main__":
    main()
