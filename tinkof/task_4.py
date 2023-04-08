n = int(input())
c = list(map(int, input().split()))

j = 1
k = 1
while k:
    a = []
    for i in c:
        a.append(i)
    count = 0
    b = []
    b.append(j)
    for i in range(len(a)):
        b.append((b[i]) ** 2 - min(a))
        a.remove(min(a))
    for i in b:
        if i < 0:
            count += 1
    if count != 0:
        j += 1
    else:
        k = 0

print(j)
