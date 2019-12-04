import numpy as np 

def get_pieces():
    with open('piece3.txt') as piece:
        currentline = []
        for line in piece:
            currentline.append(line.split(','))
        one = currentline[0]
        one[len(one)-1]=one[len(one)-1].splitlines()[0]
        two = currentline[1]
        return one, two

def matrix(n):
    m = np.zeros((n,n))
    return m

def mark(one, two, m):
    hor = 0
    vert = 99
    m[vert][hor] = 1
    for n in one:
        d, dist = n[0], int(n[1:])

    
    return m

if __name__ == "__main__":
    one, two = get_pieces()
    m = matrix(1000)
    result = mark(one, two, m)
    print(result[99][0])