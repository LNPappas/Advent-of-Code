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

def compose_image(layers):
    index_layer, index_element, index_string = 0,0,0
    color = []
    while index_element < len(layers[0]):
        current_color = []
        if layers[index_layer][index_element][index_string] == '0':
            current_color.append('B')
            index_layer = 0
            index_string +=1
        elif layers[index_layer][index_element][index_string] == '1':
            current_color.append('W')
            index_layer = 0
            index_string +=1
        elif layers[index_layer][index_element][index_string] == '2':
            index_layer += 1

        if index_string == len(layers[0][0]):
            index_element +=1
            index_string = 0
            color.append(current_color)
            current_color = []

    return color



if __name__ == "__main__":
    layers = get_piece(25,6)
    layer = get_layer(layers)
    solution1 = get_digits(layer, layers)
    print('Part 1:', solution1)
    solution2 = compose_image(layers)

    print('Part 2:')
    for x in solution2:
        print(x)