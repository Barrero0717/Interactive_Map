import folium
import pandas

def map():
    # Read the data
    data = pandas.read_csv("bomberos_bogota.csv")
    # Extract the necessary data
    lat = list(data["latitude"])
    lon = list(data["longitude"])
    name = list(data["name"])

    # Adding HTML on Popups
    html = """<h4>Nombre:</h4>
    %s
    """

    # Create a Map with folium indicated the coordinates and the zoom_start property
    map = folium.Map(location=[4.60971, -74.08175], zoom_start=12)
    # create a group with the same map
    fg = folium.FeatureGroup(name="My Map")
    
    # Add a markers into the map, with a popup and a color
    for lt, ln, nam in zip(lat, lon, name):
        # Add the html
        iframe = folium.IFrame(html=html % str(nam), width=200, height=100)
        #Put the markers
        fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color="blue")))
    
    map.add_child(fg)
    # Save the map in a file
    map.save("Map1.html")

if __name__ == '__main__':
    map()