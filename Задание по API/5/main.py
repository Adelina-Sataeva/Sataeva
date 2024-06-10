import requests

def find_nearest_pharmacy(address):
    api_key = 'c7977893-1e2f-4958-afd2-0d9f5b5305e7'
    try:
        geocode_response = requests.get(
            f'https://geocode-maps.yandex.ru/1.x/?apikey={api_key}&format=json&geocode={address}')
        geocode_response.raise_for_status()
        location = geocode_response.json()
        if 'GeoObjectCollection' in location and 'featureMember' in location['GeoObjectCollection']:
            coordinates = location['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
            longitude, latitude = map(float, coordinates.split())

            response = requests.get(f'https://example.com/api/pharmacies?lat={latitude}&lon={longitude}')
            response.raise_for_status()
            nearest_pharmacy = response.json()
            print(f"Ближайшая аптека: {nearest_pharmacy['name']}")
        else:
            print("Координаты не найдены для указанного адреса.")

    except requests.exceptions.HTTPError as err:
        print("Ошибка HTTP при запросе к API:", err)

    except Exception as ex:
        print("Произошла ошибка:", ex)

address = input("Введите адрес: ")
find_nearest_pharmacy(address)