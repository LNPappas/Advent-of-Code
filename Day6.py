def get_pieces():
    with open('piece6.txt') as piece:
        first, second = [], []
        for number in piece:
            if number[-1] == '\n':
                number = number[:-1] 
            
            first.append(number[:3])
            second.append(number[4:])
    return first, second

if __name__ == "__main__":
    a, b = get_pieces()
    print(a[0], b[0])