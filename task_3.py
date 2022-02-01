lenght = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
count = 0
pred = -1

while 1:
    if lenght == 0:
        print(count)
        break
    else:
        up = a[lenght - 1]
        down = b[lenght - up - 1]

        lenght = lenght - (up - down)
        count += 1

        if lenght == pred:
            print('-1')
            break
        pred = lenght
