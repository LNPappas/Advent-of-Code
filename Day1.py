def get_pieces():
    with open('piece1.txt') as piece:
        puzzle = []
        for number in piece:
            l = len(number)-1
            number = number[:l] 
            puzzle.append(int(number))
    return puzzle

def calc_fuel(mass):
    return (mass//3)-2

def calc_mass(puzzle):
    total = 0
    for mass in puzzle:
        fuel = calc_fuel(mass)
        while fuel > 0:
            total = total+fuel
            fuel = calc_fuel(fuel)
    return total

if __name__ == "__main__":
    mass = get_pieces()
    solution = calc_mass(mass)
    print(solution)