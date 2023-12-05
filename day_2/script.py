from collections import defaultdict

def part_1(line):
    game, record = line.split(': ')
    game_id = int(game.split(' ')[1])
    sets = record.split('; ')
    
    for hand in sets:
        cubes = hand.split(', ')
        cube_dict = {}
        for cube in cubes:
            num, color = cube.split(' ')
            color = color.strip()
            if color not in cube_dict:
                cube_dict[color] = 0
            cube_dict[color] += int(num) 
        
        if not check(cube_dict):
            return 0

    return game_id

def check(cubes_dict):
    for color in cubes_dict:
        if cubes_dict[color] > game_constraint[color]:
            return False
    return True

def part_2(line):
    game, record = line.split(': ')
    sets = record.split('; ')

    cubes_dict = defaultdict(int)
    
    for hand in sets:
        cubes = hand.split(', ')
        for cube in cubes:
            num, color = cube.split(' ')
            color = color.strip()
            cubes_dict[color] = max(cubes_dict[color], int(num))
    
    return calculate_prod(cubes_dict)

def calculate_prod(cube_dict):
    prod = 1
    for color in cube_dict:
        prod *= cube_dict[color]
    return prod
        
game_constraint = {
    "red": 12,
    "blue": 14,
    "green": 13
}

sum_id = 0
with open('input.txt') as f:
    for line in f:
        res = part_1(line)
        sum_id += res
# print(sum_id)

prod_sum = 0
with open('input.txt') as f:
    for line in f:
        res = part_2(line)
        prod_sum += res
print(prod_sum)



