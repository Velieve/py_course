import folium
map = folium.Map(location=[40.474264158617714, -3.6873943838543224],tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name="my_map")
fg.add_child(folium.Marker(location=[40.4,-3.6],popup="Hi You are here!",icon=folium.Icon(color="red")))
map.add_child(fg)
map.save("Map.html")