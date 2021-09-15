import folium

def map():
    map = folium.Map(location=[4.757379055732696, -74.10607339701325], zoom_start=100)
    fg = folium.FeatureGroup(name="My Map")
    map.add_child(folium.Marker(location=[4.757379055732696, -74.10607339701325], popup="Soy un Marcador", icon=folium.Icon(color="blue")))
    map.add_child(fg)
    map.save("Map1.html")

if __name__ == '__main__':
    map()