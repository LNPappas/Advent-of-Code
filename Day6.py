class Body(object):
    def __init__(self, name, parent):
        self.children = []
        self.name = name
        self.parent = parent

def add_chidren(body, orbits):
    r = [orbit for orbit in orbits if orbit.startswith(body.name)]

    for c in r:
        orbits.remove(c)
        c_name = c.split(')')[1]
        c_body = Body(c_name, parent=body)
        body.children.append(c_body)
        add_chidren(c_body, orbits)

def count(body, dist=1):
    return len(body.children)*dist + sum([count(c_body, dist+1) for c_body in body.children])

def get_parent(node, b_name, result):
    for child in node.children:
        if child.name == b_name:
            result.append(node)
        else:
            get_parent(child, b_name, result)

def get_child(node, name_node, dist=0):
    for child in node.children:
        if child.name == name_node:
            return dist
        else:
            result = get_child(child, name_node, dist+1)
            if result is not None:
                return result

def dist_node(p_node, name_node):
    result = get_child(p_node, name_node)
    if result is None:
        return 1+ dist_node(p_node.parent, name_node)
    return result

def get_pieces():
    with open('piece6.txt') as piece:
        orbits = []
        for x in piece:
            if x[-1] == '\n':
                x = x[:-1] 
            orbits.append(x)
    return orbits

if __name__ == "__main__":
    orbits = get_pieces()
    com = Body('COM', None)
    add_chidren(com, orbits)
    print('Part 1:', count(com))

    result = []
    get_parent(com, 'YOU', result)
    you_parent = result[0]
    print('Part 2:', dist_node(you_parent, 'SAN'))