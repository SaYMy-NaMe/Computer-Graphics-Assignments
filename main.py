def slope_less_than_one(point1, point2):
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
            p = p + 2*dy
        else:
            p = p + 2*dy - 2*dx
            y += 1
    print(all_points)
    print(all_p)


def slope_greater_than_one(point1, point2):
    print('Slope is greater or equal one')


def bresenham_line(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dy = y2 - y1
    dx = x2 - x1
    if dy < dx:
        slope_less_than_one(point1, point2)
    else:
        slope_greater_than_one(point1, point2)


def inputCoordinates():
    print('Input the First Coordinate: ')
    x1 = int(input('Enter the X1: '))
    y1 = int(input('Enter the Y1: '))
    print('\n')
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
    point2 = [5, 8]
    bresenham_line(point1, point2)

    # Actual Data
    # n = int(input('How many cases do you have?: '))
    # for i in range(n):
    #     inputCoordinates()


if __name__ == "__main__":
    main()
