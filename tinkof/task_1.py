n, m = map(int, input().split())

count = 0
while 1:
    if n < m:
        m -= n
        count += 1
    elif n > m:
        n -= m
        count += 1
    elif n == m:
        count += 1
        print(count)
        break
