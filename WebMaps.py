import folium
import pandas
data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

def icon_color(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


html = """<h4>Volcano information:</h4>
Height: %s m
"""


mymap=folium.Map(location=[38.58,-99.09],zoom_start=6, tiles = "Stamen Terrain") #Base Layer
# Its good to declare a featuergroup for easiness
fgv=folium.FeatureGroup(name="Volcanoes") #Marker layer
for lt,ln,elv in zip(lat,lon,elev):
   fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(elv)+" m", fill_color=icon_color(elv), color='grey', fill_opacity=0.7 ))     #icon=folium.Icon(color=icon_color(elv)

fgp=folium.FeatureGroup(name="World poplulation") #Polygon layer

fgp.add_child(folium.GeoJson(data=(open('world_pop.json', 'r', encoding='utf-8-sig').read()), 
style_function=lambda x: {'fillColor': 'yellow' if x['properties']['POP2005'] <= 10000000
else 'red'if 10000000 <= x['properties']['POP2005'] < 20000000 else 'pink'}))

mymap.add_child(fgv)
mymap.add_child(fgp)
mymap.add_child(folium.LayerControl())
mymap.save("WebMap.html")


#fill_opacity is for transperancy
    #fg.add_child(folium.Marker(location=[lt,ln], popup=str(elv)+" m", icon=folium.Icon(color=icon_color(elv))))
#2nd task, plotting all countries boundries in polygon layer.
#3 layers on web page, 1-Map tiles(Base Layer just a map), 2-Marker layers,3-polygon or shape layers
























#:::::::::::: Practice commands and help items



#mymap.add_child(folium.Marker(location=[38.2,-99.1], popup="I am a marker", icon=folium.Icon(color='blue')))
#>>> import folium
# >>> dir(folium)
# >>> help(folium.Map)
# >>> map1=folium.Map(location=[60.29,25.04], width=800, height=700)
# >>> map1.save("Map.html")
# >>> map1=folium.Map(location=[60.29,25.04], width=800, height=700, max_zoom=200)
# >>> map1.save("Map.html")
# >>> map1=folium.Map(location=[60.29,25.04], width=800, height=700, max_zoom=50)
# >>> map1.save("Map.html")

#::::::::::::::ZIP TWO ITEMS::::::

# >>> for i,j in zip([2,3,5],[1,2,3]): 
# ...     print(i,"and",j)
# ... 
# 2 and 1
# 3 and 2
# 5 and 3
# ::::.Lambda fucntion practice
# >>> l=lambda x: x**2
# >>> l(5)