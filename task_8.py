import math


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


pair = [0, 0]
min_nok = 10 ** 9
n = 9
l1 = [i for i in range(1, n + 1)]
l2 = [i for i in range(1, n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j == n and sorted([i, j]) != pair:
            if lcm(i, j) < min_nok:
                pair = sorted([i, j])
                min_nok = lcm(i, j)
print(pair[0], pair[1])
