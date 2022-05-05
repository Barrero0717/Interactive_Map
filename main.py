import folium
import pandas

def map():
    # Read and extract the firefighters data
    data = pandas.read_csv("bomberos_bogota.csv")
    lat = list(data["latitude"])
    lon = list(data["longitude"])
    name = list(data["name"])
    address = list(data["address"])
    phone = list(data["phone"])

    # Adding HTML on Popups firefighters
    html = """    
    <head><style>
    body {
        font-family: Verdana, sans-serif;
    }
    </style></head>
    <body>
    <h6>Nombre: %s</h6>
    <h6>Dirección: %s</h6>
    <h6>Teléfono: %s</h6>
    </body>     
    """
  
    # Create a Map with folium indicated the coordinates and the zoom_start property
    map = folium.Map(location=[4.60971, -74.08175], zoom_start=12)
    
    # Create a localities group in the same map
    loc = folium.FeatureGroup(name="Localidades")
    # Adding Bogota localities Map Layer
    loc.add_child(folium.GeoJson(data=open("localidades.json","r",encoding="utf-8-sig").read(),popup=folium.GeoJsonPopup(fields=['LocNombre'],labels=False)))

    # Create a firefighters group in the same map
    fire = folium.FeatureGroup(name="Bomberos")
    # Add a markers into the map, with a popup and a color
    for lt, ln, nam, addr, phon in zip(lat, lon, name, address, phone):
        # Add the html
        iframe = folium.IFrame(html=html % (nam, addr,phon), width=235, height=135)
        # Put the icon markers
        # fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color="blue")))
        # Put the icon markers with circle markers
        fire.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=folium.Popup(iframe), fill_color="#8B0000", color="grey", fill_opacity=0.7 )) 

    # Create a routes in the same map
    bicycle = folium.FeatureGroup(name="Ciclorutas")
    # Adding bycicle router Map Layer
    bicycle.add_child(folium.GeoJson(data=open("RedBiciusuario.geojson","r",encoding="utf-8-sig").read(), style_function=lambda x: {'color': '#666464'}))

    # Create a police group in the same map
    police = folium.FeatureGroup(name="CAI's")
    # Add a markers into the map, with a popup and a color
    police.add_child(folium.GeoJson(data=open("CAI.geojson","r",encoding="utf-8-sig").read(), 
        popup=folium.GeoJsonPopup(fields=['CAIDESCRIP','CAIDIR_SITIO','CAITELEFON'], aliases=['Nombre:','Dirección:','Teléfono:'], style=('font-family: Verdana, sans-serif')), 
        marker=folium.CircleMarker(fill_color="green", color="grey", fill_opacity=0.7)))

    # Add the groups into the map
    map.add_child(loc)
    map.add_child(police)
    map.add_child(fire)
    map.add_child(bicycle)
    

    # Add que Layer Control
    map.add_child(folium.LayerControl())
    
    # Save the map in a file
    map.save("Map1.html")

if __name__ == '__main__':
    map()