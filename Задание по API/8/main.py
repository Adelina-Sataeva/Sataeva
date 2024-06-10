import math


def distance(lat1, lon1, lat2, lon2):
    # Переводим координаты из градусов в радианы
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Радиус Земли в километрах
    radius = 6371.0

    # Вычисляем разницу между широтами и долготами
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Вычисляем расстояние по формуле декартовой метрики
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c * 1000  # Переводим в метры

    return distance


# Ввод координат пользователем
lat1 = float(input("Введите широту дома: "))
lon1 = float(input("Введите долготу дома: "))
lat2 = float(input("Введите широту университета: "))
lon2 = float(input("Введите долготу университета: "))

# Вычисление расстояния
result = distance(lat1, lon1, lat2, lon2)
print(f"Расстояние между точками: {result} метров")
