# https://coderun.yandex.ru/seasons/first_2023/tracks/backend/problem/median-out-of-three
def main():
    numbers = sorted(list(map(int, input().split())))
    print(numbers[1])


if __name__ == "__main__":
    main()
