import folium 
import math
import fully #info
import proto #chat

proto.intro()




handy_map= folium.Map(location = [39.045753, -76.641273],zoom_start = 12)



#making markers for certain locations 
folium.Marker([38.98956913434839, -76.83772275630983], 
	popup = "<h1>High Shool</h1><img src ='DuvalHS.png'width = '400px'><p> Duval High school, a place where you can be for 8 hours if you are a student</p>",
	tooltip = 'Great school',
	icon = folium.Icon(icon = 'heart',icon_color = 'pink') ).add_to(handy_map)

lat1 = float(input('Please the firs number of option?: '))
long1 = float(input("Please enter the second num of option?:  "))
folium.Marker([lat1,long1], 
	popup = "<h1>Monument</h1><img src ='monument.jpeg'width = '400px'><p>a brave and inspiring leader born in a family of 11 with much history left behind </p>",
	tooltip = 'General William Tecumseh Sherman ',
	icon = folium.Icon(icon = 'heart',icon_color = 'blue') ).add_to(handy_map)
#make a radious around both of this locations
folium.Circle(
	location = (38.935199794334864, -76.94104593946385),
	radius = 30000,
	popup = "great place to go around",
	color = 'Blue',
	fill = True,
	fill_color = 'yellow').add_to(handy_map) 



handy_map.save('map.html')


