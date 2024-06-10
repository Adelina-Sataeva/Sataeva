def find_southernmost_city():
    cities = input("Введите список городов через запятую: ").split(",")
    cities = [city.strip() for city in cities]  # Удаляем пробелы после запятой

    southernmost_city = min(cities, key=lambda x: x.lower())  # Находим самый южный город
    print(f"Самый южный город: {southernmost_city}")

find_southernmost_city()
