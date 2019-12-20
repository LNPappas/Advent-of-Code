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
    layer, height, pixel = 0,-1,0
    pixels = []
    while height < 5:
        height +=1
        pixel = 0
        while pixel < 25:
            if layers[layer][height][pixel] == '0':
                pixels.append(' ')
                layer = 0
                pixel +=1            
            elif layers[layer][height][pixel] == '1':
                pixels.append('1')
                layer = 0
                pixel +=1
            else:
                layer +=1
    return pixels

def compose_layers(pixels):
    temp = ''.join(pixels)
    n = 25
    image = [temp[i:i+n] for i in range(0, len(temp), n)]
    return image

if __name__ == "__main__":
    layers = get_piece(25,6)
    layer = get_layer(layers)
    solution1 = get_digits(layer, layers)
    print('Part 1:', solution1)
    pixels = compose_image(layers)
    solution2 = compose_layers(pixels)
    print('Part 2:')
    for l in solution2:
        print(l)