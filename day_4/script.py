from collections import defaultdict

def part_1(line):
    pts = 0
    has_one = False

    card, nums = line.split(': ')
    win_nums, hand = nums.split(' | ')
    win_nums, hand = convert(win_nums, hand)

    for num in hand:
        has_one = True
        if num in win_nums:
            if not pts:
                pts = 1
            else:
                pts *= 2
    
    return pts if has_one else 0
    
def convert(arr1, arr2):
    return (arr1.strip().split(), arr2.strip().split())

def part_2(line):
    card, nums = line.split(': ')
    card_num = card.strip(':').split()[1]
    win_nums, hand = nums.split(' | ')
    win_nums, hand = convert(win_nums, hand)

    copies[card_num] += 1
    start = int(card_num) + 1

    for num in hand:
        if num in win_nums:
            for _ in range(copies[card_num]):
                copies[str(start)] += 1
            start += 1

# pts = 0
# with open('test.txt', 'r') as f:
#     for line in f:
#         pts += part_1(line)
# print(pts)

copies = defaultdict(int)
with open('input.txt', 'r') as f:
    for line in f:
        part_2(line)

res = 0
for num in copies:
    res += copies[num]
print(res)



