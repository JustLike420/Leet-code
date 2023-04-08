# https://coderun.yandex.ru/seasons/first_2023/tracks/backend/problem/sorting-reverse-order
import requests

import json


def main():
    url = input()
    port = input()
    a = input()
    b = input()
    response = requests.get(url=f'{url}:{port}', params={'a': a, 'b': b})
    data = json.loads(response.text)
    data.sort(reverse=True)
    new_data = []
    for el in data:
        if el >= 0:
            new_data.append(str(el))

    print('\n'.join(new_data))


if __name__ == "__main__":
    main()
