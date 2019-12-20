'''
Day 10:
    . = empty
    # = asteroid

    x = distance from left
    y = distance from top
'''

def piece():
    l = []
    temp = ''
    with open('piece9.txt') as piece:
        for x in piece:
            temp += x
            l = temp.split('\n')
    return l

def dimentions(l):
    width = len(l[0])
    height = len(l)
    print(width, 'x', height)

if __name__ == "__main__":
    p = piece()
    dimentions(p)
    # for n in p:
    #     print(n)

