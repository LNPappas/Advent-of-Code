import numpy as np 
import matplotlib.pyplot as plt
import string

def get_pieces():
    with open('piece3.txt') as piece:
        currentline = []
        for line in piece:
            currentline.append(line.split(','))
        one = currentline[0]
        one[len(one)-1]=one[len(one)-1].splitlines()[0]
        two = currentline[1]
        return one, two

def get_plots(arr):
    x, y = 0,0
    plots = []

    for temp in arr:
        direction, distance = temp[0], int(temp[1:])
        if direction == 'U':
            y += distance
        elif direction == 'D':
            y -= distance
        elif direction == 'R':
            x += distance
        elif direction =='L':
            x-= distance
        plots.append((x,y))
    return plots

def get_index(one):
    close_x = -325
    close_y = -384
    match = []
    for index, check in enumerate(one):
        if check[0] < close_x and check[1] < close_y:
            match.append(index)

    return match

def get_steps(arr, num):
    total = num
    for x in arr:
        x = x[1:]
        total += int(x)
    return total

if __name__ == "__main__":
    one, two = get_pieces()

    # one = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
    # two = ['U62','R66','U55','R34','D71','R55','D58','R83']

    # one = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
    # two = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']

    plot_one = get_plots(one)
    plot_two = get_plots(two)
    result_one = get_index(plot_one)
    result_two = get_index(plot_two)
    # print(result_one)
    # print(result_two)

    plt.plot(*zip(*plot_one[:15]), *zip(*plot_two[:12]))
    plt.show()
    print(one[13], one[14])
    print(plot_one[13], plot_one[14])
    print(two[10], two[11])
    print(plot_two[10], plot_two[11])

    r1 = get_steps(one[:14], 84)
    r2 = get_steps(two[:11], 401)
    print(r1+r2)

