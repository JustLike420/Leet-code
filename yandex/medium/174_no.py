# https://coderun.yandex.ru/seasons/first_2023/tracks/backend/problem/buses-ya-intern

def main():
    n = int(input())
    flight_intervals = list(map(int, input().split()))

    total_expected_wait_time = 0
    for i, interval in enumerate(flight_intervals):
        expected_wait_time = (interval // 2) * (i+1)
        total_expected_wait_time += expected_wait_time

    print(f"{total_expected_wait_time}/{n}")


if __name__ == "__main__":
    main()
