# https://coderun.yandex.ru/seasons/first_2023/tracks/backend/problem/dayofweek-ya-intern
from datetime import date
import calendar
import sys


def main():
    days = calendar.day_name
    months = {month: index for index, month in enumerate(calendar.month_name) if month}
    while True:
        try:
            input_date = input().split()
            day = date(int(input_date[2]), months[input_date[1]], int(input_date[0])).weekday()
            print(days[day])
        except EOFError:
            sys.exit()


if __name__ == "__main__":
    main()
