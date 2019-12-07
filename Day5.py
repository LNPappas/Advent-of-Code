l = []
output = []

def data():
    with open('piece5.txt') as piece:
        for num in piece:
            l = num.split(',')
        return l

def op1(mode1, mode2, mode3, p1, p2, p3):
    first, second, third, = 0,0,0
    if mode1 == 0:
        first = l[p1]
    elif mode1 == 1:
        first = p1
    if mode2 == 0:
        second = l[p2]
    elif mode2 == 1:
        second = p2

    third = int(p3)
    print(first, second)
    print('equals:', str(int(first)+int(second)))
    l[third] = str(int(first)+int(second))
    return True

def op2(mode1, mode2, mode3, p1, p2, p3):
    first, second, third, = 0,0,0
    if mode1 == 0:
        first = l[p1]
    elif mode1 == 1:
        first = p1
    if mode2 == 0:
        second = l[p2]
    elif mode2 == 1:
        second = p2

    third = int(p3)
    l[third] = str(int(first)*int(second))
    print(first, second)
    print('equals:', str(int(first)+int(second)))
    return True

def op3(p1):
    i = input("What is your input?")
    l[p1] = i
    return True

def op4(mode1, p1):
    if mode1 == 0:
        output.append(l[p1])
    else:
        output.append(p1)
    return True

def op5(i, mode1, mode2, p1, p2):
    print('\nop5')
    if mode1 == 0:
        one = l[p1]
    elif mode1 == 1:
        one = p1

    if mode2 == 0:
        two = l[p2]
    elif mode2 == 1:
        two = p2


    if int(one) != 0:
        i = int(two)
    else:
        i += 3
    return i

def op6(i, mode1, mode2, p1, p2):
    print('\nop6')
    if mode1 == 0:
        one = l[p1]
    elif mode1 == 1:
        one = p1

    if mode2 == 0:
        two = l[p2]
    elif mode2 == 1:
        two = p2

    if int(one) == 0:
        i = int(two)
    else:
        i += 3
    return i

def op7(mode1, mode2, p1, p2, p3):
    print('\nop7')
    if mode1 == 0:
        one = int(l[p1])
    elif mode1 == 1:
        one = p1

    if mode2 == 0:
        two = int(l[p2])
    elif mode2 == 1:
        two = p2

    if one <= two:
        l[p3] = '1'
    else:
        l[p3] = '0'

    return True

def op8(mode1, mode2, p1, p2, p3):
    print('\nop8')
    if mode1 == 0:
        one = int(l[p1])
    elif mode1 == 1:
        one = p1

    if mode2 == 0:
        two = int(l[p2])
    elif mode2 ==1:
        two = p2

    if one == two:
        l[p3] = '1'
    else:
        l[p3] = '0'
    return True


def get_op(num):
    if num == '99':
        return int(99)
    else:    
        return int(num[-1])

def process():
    position = 0
    while position < len(l):
        current = l[position]
        print('position:', position, ' l[position]:', l[position])
        temp = ''
        if len(l[position]) > 1:
            temp = l[position][:-2]
        mode1, mode2, mode3 = 0,0,0
        if temp == '':
            pass
        elif len(temp) == 1:
            mode1 = int(temp[0])
        elif len(temp) == 2:
            mode1, mode2 = int(temp[1]),int(temp[0])
        else:
            mode1, mode2, mode3 = int(temp[2]),int(temp[1]),int(temp[0])

        print('mode1:', mode1, ' mode2:', mode2, ' mode3:', mode3)
        op = get_op(current[-2:])
        print(current)

        if op == 1: 
            p1 = int(l[position+1]) 
            p2 = int(l[position+2])     
            p3 = int(l[position+3])     
            op1(mode1, mode2, mode3, p1, p2, p3)
            position += 4
        elif op == 2:
            p1 = int(l[position+1])
            p2 = int(l[position+2])
            p3 = int(l[position+3])
            op2(mode1, mode2, mode3, p1, p2, p3)
            position += 4
        elif op == 3:
            p1 = int(l[position+1])
            op3(p1)
            position += 2
        elif op == 4:
            p1 = int(l[position+1])
            op4(mode1, p1)
            position += 2
        elif op == 5:
            p1 = int(l[position+1])
            p2 = int(l[position+2])
            position = op5(position,mode1, mode2, p1,p2)
        elif op == 6:
            p1 = int(l[position+1])
            p2 = int(l[position+2])
            position = op6(position,mode1, mode2, p1,p2)
        elif op == 7:
            p1 = int(l[position+1])
            p2 = int(l[position+2])
            p3 = int(l[position+3])
            op7(mode1, mode2, p1,p2,p3)
            position += 4
        elif op == 8:
            p1 = int(l[position+1])
            p2 = int(l[position+2])
            p3 = int(l[position+3])
            op8(mode1, mode2, p1,p2,p3)
            position +=4
        elif op == 99:
            break
        # print(l)
if __name__ == "__main__":
    l = data()
    # l = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
    #     1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
    #     999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    # l = [str(x) for x in l]

    # l = ['3','12','6','12','15','1','13','14','13','4','13','99','-1','0','1','9']
    # l = ['3','3','1105','-1','9','1101','0','0','12','4','12','99','1']
    # l = [2,0,0,0,99]
    # l = [str(x) for x in l]
    # print(l)
    process()
    o = [int(x) for x in output]
    print(o)