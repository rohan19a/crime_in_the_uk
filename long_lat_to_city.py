from main import police_df
import geopy
from geopy.geocoders import Nominatim
from geopy.point import Point


geolocator = Nominatim(user_agent="geoapiExercises")

#select the columns "Longitude" ,"Latitude" from police_df

new_police_df = police_df[["Longitude","Latitude"]]
new_police_df.dropna(how='all', axis=1, inplace=True)


#return a list of tuples from new_police_df
new_police_df_list = new_police_df.values.tolist()
#print(new_police_df_list)

for x in new_police_df_list: 
    location = geolocator.reverse(Point(x[1],x[0]))
    print(location)
    #print(str(x[1])+","+str(x[0]))



#location = geolocator.reverse(Latitude+","+Longitude)
 
# Display
#print(location)
