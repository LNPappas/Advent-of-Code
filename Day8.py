def get_piece(width, height):
    layers = []
    with open('piece8.txt') as piece:
        for x in piece:
            layers.append(x)
    temp = layers[0]
    layers = [temp[i:i+width] for i in range(0, len(temp), width)]
    layers_height = [layers[i:i+height] for i in range(0, len(layers), height)]
    return layers_height


def get_layer(layers):
    l = [0]*len(layers)
    i = 0
    while i < len(layers):
        total = 0
        temp = ''.join(layers[i])
        for x in temp:
            if x == '0':
                total +=1
        l[i] = total
        total = 0
        i +=1
    return l.index(min(l))


def get_digits(layer, layers):
    temp = ''.join(layers[layer])
    one = 0
    two = 0
    for x in temp:
        if x == '1':
            one += 1
        elif x == '2':
            two +=1
    return one*two

if __name__ == "__main__":
    layers = get_piece(25,6)
    layer = get_layer(layers)
    solution = get_digits(layer, layers)
    print(layer)
    print(solution)