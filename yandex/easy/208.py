# https://coderun.yandex.ru/seasons/first_2023/tracks/backend/problem/merge-jsons-2
import json


def main():
    n, m = map(int, input().split())
    offers = []
    for _ in range(n):
        offers.extend(json.loads(input())['offers'])
    print(json.dumps({'offers': offers[:m]}, indent=4))


if __name__ == "__main__":
    main()
