import re

step = []
vel = []


def piece():
    global step 
    global vel
    l = []
    temp = ''
    with open('piece12.txt') as piece:
        for x in piece:
            temp += x
            l = temp.split('\n')
        for index, value in enumerate(l):
            temp = []
            temp = re.findall(r'-?\d+', value) 
            res = list(map(int, temp)) 
            l[index] = temp
    step = l
    vel = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]

def time_step(n):
    i = 0
    while i < n:
        velocity()

def velocity():
    pass
    # t1 = []
    # t2 = []
    # for a in m1 and b in m2:
    #     if a > b:
    #         a-=1
    #         b+=1
    #     elif a < b:
    #         a+=1
    #         b-=1
    #     else:
    #         pass
    #     t1.append(a)
    #     t2.append(b)
    


def position(p, v):
    temp = []
    for a in p and b in v:
        temp.append(a+b)
    return temp

def total_energy():
    i_s = sum([abs(e) for e in io_step])
    i_v = sum([abs(e) for e in io_vel])
    i_total = i_s*i_v

    e_s = sum([abs(e) for e in europa_step])
    e_v = sum([abs(e) for e in europa_vel])
    e_total = e_s*e_v

    g_s = sum([abs(e) for e in ganymede_step])
    g_v = sum([abs(e) for e in ganymede_vel])
    g_total = g_s*g_v

    c_s = sum([abs(e) for e in callisto_step])
    c_v = sum([abs(e) for e in callisto_vel])
    c_total = c_s*c_v

    return i_total+e_total+g_total_c_total


if __name__ == "__main__":
    data = piece()
    time_step(1)

    print(step[3], vel[3])
