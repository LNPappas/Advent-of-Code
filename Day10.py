'''
Day 10:
    . = empty
    # = asteroid

    x = distance from left
    y = distance from top
'''

total = 0

def piece():
    l = []
    temp = ''
    with open('piece10.txt') as piece:
        for x in piece:
            temp += x
            l = temp.split('\n')
    return l

def asteroid_count(belt):
    global total
    temp = [item for sublist in belt for item in sublist]
    for item in temp:
        if item == '#':
            total +=1
    print('Total:', total)


def coordinates(belt):
    highest = 0
    best_view = (0,0)
    x, y = 0, 0
    while y < len(belt):
        for position in belt[y]:
            if position == '#':
                v = view(x, y, belt)
                if v > highest:
                    print('asteroids:', v)
                    highest = v
                    best_view = (x,y)
            x+=1
        y +=1
        x = 0
    print(highest)
    return best_view

def view(x,y,belt):
    asteroid = 1
    print('(x,y):', x, ',', y)
    j = x
    k = y
    while (k+y) < len(belt) and (j+x) < len(belt[0]):
        temp = j
        if belt[k][j] == '#':
            while temp < len(belt[0]):
                if belt[k][temp] == '#':
                    asteroid +=1
                temp+=1
        j+=x
        k+=y
    
    j = x-x
    k = y-y
    while (k-y) > 0 and (j-x) > 0:
        temp = j
        if belt[k][j] == '#':
            while temp > 0:
                if belt[k][temp] == '#':
                    asteroid +=1
                temp -=1
        j-=x
        k-=y

    j = x+x
    k = y-y
    while (k-y) > 0 and (j+x) < len(belt[0]):
        temp = j
        if belt[k][j] == '#':
            while temp < len(belt[0]):
                if belt[k][temp] == '#':
                    asteroid +=1
                temp+=1
        j+=x
        k-=y

    j = x-x
    k = y+y
    while (k+y) < len(belt) and (j-x) > 0:
        temp = j
        if belt[k][j] == '#':
            while temp > 0:
                if belt[k][temp] == '#':
                    asteroid +=1
                temp -=1
        j-=x
        k+=y
    print('asteroid:', asteroid)
    print('total_asteroids:', total-asteroid)
    return total-asteroid
            


if __name__ == "__main__":
    p = piece()
    asteroid_count(p)
    best = coordinates(p)
    print(best)
    

