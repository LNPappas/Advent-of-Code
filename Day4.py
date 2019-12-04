# piece 4: range = 240298-784956
# 2 consecutive digits, always increaseing 

def initial_range():
    l = [x for x in range(240298, 784956)]
    return l

def consecutive_check(l):
    l1 = [str(x) for x in l]
    l2 = []
    for x in l1:
        for index, value in enumerate(x):
            if index != 0:
                if int(value) >= int(x[index-1]):
                    if index == len(x)-1:
                        l2.append(x)
                else:
                    break
    return l2

def double_check(l):
    l3 = []
    for word in l:
        d = {}
        good = False
        for letter in word:
            if letter in d:
                d[letter] +=1
            else:
                d.update({letter:1})
        for value in d.values():
            if 2 == value:
                good = True
                break
        if good == True:
            l3.append(word)
    return l3

if __name__ == "__main__":
    l = initial_range()
    l2 = consecutive_check(l)
    l3 = double_check(l2)
    print(l3)
    print(len(l3))
