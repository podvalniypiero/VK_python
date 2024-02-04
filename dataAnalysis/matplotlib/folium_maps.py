import folium

import folium.plugins as plugins

from folium.plugins import MarkerCluster
from folium.plugins import MousePosition
from folium.features import DivIcon

import pandas as pd

# define the world map
world_map = folium.Map()
world_map
world_map.save('files/world_map.html')

# define the Russia map
russia_map = folium.Map(
    location = [64.6863136, 97.7453061],    # широта и долгота России
    zoom_start = 4                          # начальный уровень масштабирования
)
russia_map.save('files/russia_map.html')


partizan = pd.read_excel('files/partizan.xlsx')
print(partizan.tail())

# Folium - библиотека для визуализации интерактивных карт - для визуализации гео-пространственных данных - создать карту любого местоположения, зная широту и долготу
# создать карту и наложить маркеры, кластер маркеров

lats = list(partizan.lat)
longs = list(partizan.lon)
places=[[x[0],x[1]] for x in zip(lats,longs)]

m = folium.Map(places[0], tiles = 'OpenStreetMap', zoom_start=13)

# plugins.MarkerCluster(places).add_to(m)
# plugins.BoatMarker(places[0]).add_to(m)
plugins.FastMarkerCluster(places).add_to(m)

m.save('files/m.html')







