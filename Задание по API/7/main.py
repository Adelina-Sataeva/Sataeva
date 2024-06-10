import requests
import sys


def get_district(address):
    api_key = 'c7977893-1e2f-4958-afd2-0d9f5b5305e7'
    try:
        response = requests.get(f'http://geocoder/api?kind=district&lat={lat}&lon={lon}')
        if response.status_code == 200:
            district = response.json()['district']
            return district
        else:
            return 'Ошибка при запросе к геокодеру'
    except Exception as e:
        return f'Произошла ошибка: {str(e)}'


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('введите адрес в командной строке:')
    else:
        address = ' '.join(sys.argv[1:])
        district = get_district(address)
        print(f'Район для адреса {address}: {district}')