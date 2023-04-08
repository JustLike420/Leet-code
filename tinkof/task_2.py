A, B, n = map(int, input().split())
if (A - B) % 2 == 0 and (A - B) >= 2 * n:
    print('YES')
else:
    print('NO')
