import folium
stadiums_location = {"Лужники": "37.554191,55.715551",
                     "Спартак": "37.440262,55.818015",
                     "Динамо": "37.559809,55.791540"}
# Карта Москвы
m = folium.Map(location=[55.755825, 37.617635], zoom_start=11)

for stadium, coords in stadiums_location.items():
    lat, lon = map(float, coords.split(','))
    folium.Marker(location=[lon, lat], popup=stadium).add_to(m)

m.save("1.html")
