from itertools import combinations as cwr

num = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
money = iter(num)
combinations_list = set(m for m in cwr(money, len(num)) if sum(m) == 100)
for n in combinations_list:
    print(n)
