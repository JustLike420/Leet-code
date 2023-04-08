# https://coderun.yandex.ru/seasons/first_2023/tracks/backend/problem/rocks-and-jewels
def main():
    j = input()
    s = input()
    count = sum(_ in j for _ in s)

    print(count)


if __name__ == "__main__":
    main()
