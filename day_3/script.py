from pprint import PrettyPrinter
from collections import defaultdict

def part_1(arr):
    # (row, col)
    directions = [ [0,1], [1,0], [0,-1], [-1,0], [-1,-1], [-1, 1], [1, 1], [1,-1] ]
    curr_num = ''
    part_num = []

    i, j = 0, 0

    while i < len(arr):
        while j < len(arr[i]):
            if not arr[i][j].isdigit():
                curr_num = ''
                # print(arr[i][j], end = ": ")
            else:
                curr_num += arr[i][j]

                for direction in directions:
                    row = i + direction[0]
                    col = j + direction[1]
                    
                    if row < 0 or col < 0 or row >= len(arr) or col >= len(arr[i]):
                        continue
                    
                    # print(arr[row][col], end = " ")
                    if arr[row][col] in special_chars:
                        # get rest of digits and append to part_num
                        j = j + 1
                        while j < len(arr[i]) and arr[i][j].isdigit():
                            curr_num += arr[i][j]
                            j += 1
                        
                        part_num.append(int(curr_num))
                        curr_num = ''
                        break
            j += 1
        i += 1
        j = 0
        # print(i, j, len(arr))
            
    return part_num

def populate():
    schematic = []
    with open('input.txt', 'r') as f:
        for line in f:
            row = []
            for char in line:
                if char != '\n':
                    row.append(char)
            schematic.append(row)
    return schematic

def part_2(arr):
    directions = [ [0,1], [1,0], [0,-1], [-1,0], [-1,-1], [-1, 1], [1, 1], [1,-1] ]
    curr_num = ''
    star_idx = defaultdict(list)

    i, j = 0, 0

    while i < len(arr):
        while j < len(arr[i]):
            if not arr[i][j].isdigit():
                curr_num = ''
                # print(arr[i][j], end = ": ")
            else:
                curr_num += arr[i][j]

                for direction in directions:
                    row = i + direction[0]
                    col = j + direction[1]
                    
                    if row < 0 or col < 0 or row >= len(arr) or col >= len(arr[i]):
                        continue
                    
                    # print(arr[row][col], end = " ")
                    if arr[row][col] == '*':
                        # get rest of digits 
                        j = j + 1
                        while j < len(arr[i]) and arr[i][j].isdigit():
                            curr_num += arr[i][j]
                            j += 1
                        
                        star_idx[(row, col)].append(curr_num)
                        curr_num = ''
                        break
            j += 1
        i += 1
        j = 0
    
    return star_idx

def calculate_ratio(star_idx):
    ratio_sum = 0

    for key in star_idx:
        if len(star_idx[key]) == 2:
            ratio_sum += int(star_idx[key][0]) * int(star_idx[key][1])
    
    return ratio_sum
        

schematic = populate()
special_chars = set('*#+$@/=!%=-^&')
# print(special_chars)

# iterate through adjacent cells
# append each digit as you iterate
# if there is a special character, append digits 
s1 = sum(part_1(schematic))
# print(s1)

s2 = calculate_ratio(part_2(schematic))
print(s2)



# pp = PrettyPrinter()
# pp.pprint(schematic)

