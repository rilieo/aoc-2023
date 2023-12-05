import re

def part_1(line):
    num = re.sub('\D', '', line)
    return num

def part_2(line):
    new_line = ''
    word = ''
    for i in range(len(line)):
        word += line[i]

        if len(word) >= 3:
            for key in nums_key:
                if key in word:
                    new_line += str(nums_key[key])
                    word = line[i]
                    break

        if line[i].isdigit():
            new_line += line[i]

nums_key = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

pt1_sum = 0
with open ('input.txt', 'r') as f:
    for line in f:
        first_digit = part_1(line)[0]
        last_digit = part_1(line)[-1]

        num = first_digit + last_digit
        pt1_sum += int(num)

pt2_sum = 0
with open('input.txt', 'r') as f:
    for line in f:
        new_line = part_2(line)
        first_digit = part_1(new_line)[0]
        last_digit = part_1(new_line)[-1]

        num = first_digit + last_digit

        # print(num)
        pt2_sum += int(num)

print(pt2_sum)





