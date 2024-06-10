from PIL import Image, ImageDraw

x = float(input("Координата x объекта: "))
y = float(input("Координата y объекта: "))

def get_gps_coordinates(coordinates):
    # Logic for creating a satellite image
    image = Image.new('RGB', (100, 100), color='red')
    draw = ImageDraw.Draw(image)  # Initialize the draw variable

    # Round the object coordinates
    draw.point((round(coordinates[0]), round(coordinates[1])), fill="white")
    try:
        image.save('Снимок.png')
        print('снимок объекта сохранен в файл Снимок.png')
    except Exception as error:
        print('Ошибка сохранения снимка: {error}')

get_gps_coordinates((x, y))
