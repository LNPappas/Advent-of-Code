def get_pieces():
    with open('piece2.txt') as piece:
        for line in piece:
            currentline = line.split(',')
        return [int(x) for x in currentline]

def restore(code,a=12,b=2):
    code[1] = a
    code[2] = b
    return code

def op_code(code, spot=0):
    if code[spot] == 99:
        pass
    else:
        opt(code, spot)
    return code[0]
        
def opt(code, spot):
    op = code[spot]
    first = code[code[spot+1]]
    second = code[code[spot+2]]
    third = code[spot+3]
    if op == 1:
        code[third] = first+second
    elif code[spot] == 2:
        code[third] = first*second
    op_code(code, spot+4)

if __name__ == "__main__":
    code = get_pieces()
    reset = restore(code, a=39, b=51)
    print(op_code(reset))
    print(100*39+51)


