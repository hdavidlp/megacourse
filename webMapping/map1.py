from turtle import fillcolor, width
import folium
import pandas

def color_producer(current_status):
     color_generated = "none"
     if current_status=="Reportada":
          color_generated = "red"
     elif current_status=="Atendida":
          color_generated = "green"
     else:
          color_generated = "gray"
     
     print (f"{current_status}  {color_generated}")
     return color_generated

data = pandas.read_csv("marks.txt")
lat = list(data["Lat"])
lon = list(data["Lon"])
typ = list(data["Type"])
status = list(data["Status"])

html = """Con vinculo:<br>
<a href="https://www.google.com" target="_blank">Fuga</a><br>
Status: %s  
"""

map = folium.Map(location=[30.98,-110.28], zoom_start = 14)

# Add terrain to map
#map = folium.Map(location=[30.98,-110.28], zoom_start = 6, tiles="Stamen Terrain"

fgPopulation = folium.FeatureGroup(name="Population")
fgPopulation.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
               style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 
                                  else 'orange' if 10000000 <=x['properties']['POP2005']<20000000 else 'red'}  ))



fgFugas = folium.FeatureGroup(name="Fugas")
for lt, ln, ty, st in zip(lat,lon, typ, status):
     #iframe = folium.IFrame(html=html % str(ty), width=200, height=100)
     iframe = folium.IFrame(html=html % str(st), width=200, height=100)
     color_def = color_producer(st)
     # Agrega Puntos
     fgFugas.add_child(folium.CircleMarker(location=[lt,ln], radius = 8, popup=folium.Popup(iframe), 
                        fill_color = color_def, color = "gray", fill_opacity=0.7))
                        
     # Agrega llamadas    
     #fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), 
     #                   icon=folium.Icon(color=color_def, icon='info-sign'))) 


     # for lt, ln, ty in zip(lat,lon, typ):
     #      fg.add_child(folium.Marker(location=[lt,ln], popup=ty, icon=folium.Icon(color='green')))    


     # for coordinates in [[30.97, -110.26],[30.98, -110.30]]:
     #     fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a marker", icon=folium.Icon(color='green')))



fgFugasReportadas = folium.FeatureGroup(name="Fugas Reportadas")
fgFugasAtendidas = folium.FeatureGroup(name="Fugas Atendidas")
for lt, ln, ty, st in zip(lat,lon, typ, status):
     iframe = folium.IFrame(html=html % str(st), width=200, height=100)
     color_def = color_producer(st)
     if st == "Reportada":  
          fgFugasReportadas.add_child(folium.CircleMarker(location=[lt,ln], radius = 8, popup=folium.Popup(iframe), 
                         fill_color = color_def, color = "gray", fill_opacity=0.7))
     else:
          fgFugasAtendidas.add_child(folium.CircleMarker(location=[lt,ln], radius = 8, popup=folium.Popup(iframe), 
                         fill_color = color_def, color = "gray", fill_opacity=0.7))



map.add_child(fgPopulation)
map.add_child(fgFugasReportadas)
map.add_child(fgFugasAtendidas)
map.add_child(fgFugas)

map.add_child(folium.LayerControl())





map.save("Map1.html")