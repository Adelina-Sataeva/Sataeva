from PIL import Image
import random

def get_coordinates(city_name, toponym, static=False):
    api_key = 'c7977893-1e2f-4958-afd2-0d9f5b5305e7'
    if static:
        toponym_upper_lower = toponym["boundedBy"]["Envelope"]
        toponym_upper, toponym_lower = toponym_upper_lower["lowerCorner"].split(" ")
        toponym_upper_2, toponym_lower_2 = toponym_upper_lower["upperCorner"].split(" ")
        delta_1 = round(abs(float(toponym_lower) - float(toponym_lower_2)) / 2, 6)
        delta_2 = round(abs(float(toponym_upper) - float(toponym_upper_2)) / 2, 6)
        return delta_1, delta_2
    else:
        pass

cities = ["Ekb", "Msk", "Ufa", "Tobolsk"]
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
map_api_server = "http://static-maps.yandex.ru/1.x/"

def generate_random_coordinates():
    return (random.randint(0, 100), random.randint(0, 100), random.randint(50, 200))

def guess_the_city():
    city = random.choice(cities)
    city_image = get_coordinates(city)
    city_image.show()
    guess = input("Угадайте название города: ")
    if guess.lower() == city.lower():
        print("Ответ правильный,это", city)
    else:
        print("Ответ неправильный. Правильный ответ:", city)