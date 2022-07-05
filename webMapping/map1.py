import folium

map = folium.Map(location=[30.98,-110.28], zoom_start = 14, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[30.97, -110.26], popup="Hi I am a marker", icon=folium.Icon(color='green')))

map.add_child(fg)


map.save("Map1.html")