import webbrowser, os
from gmplot import gmplot 
from pgeocode import Nominatim as Nominatim1
from geopy.geocoders import Nominatim as Nominatim2
from hack_violet.get_data import check_db_address, check_db_zip


lats = []
longs = []
cities =[]

def plot_lat_long(lats, longs, cities):   
    #plot_lat_long generates a google map and plots the location of the
    #latitude and longitude coordinates as well as the name of the location
    #Using gmplot.
      
    
    # the initial lat long and the zoom levels for the map as well as initial zoom
    gmap = gmplot.GoogleMapPlotter(lats[0], longs[0], 10)
    
    #Makes markers easier to find for windows
    if ":\\" in gmap.coloricon:
        gmap.coloricon = gmap.coloricon.replace('/', '\\')
        gmap.coloricon = gmap.coloricon.replace('\\', '\\\\')
    
    for i in range(0 , len(lats)):
        gmap.marker(lats[i], longs[i], color = "blue", title = 'Location: '+ cities[i])
    
    # get the currentdirectory
    cwd = os.getcwd()
    # saving the map as an HTML into the project directory
    gmap.draw("traceroute.html")   
    # opening the HTML via default browser
    webbrowser.open("file:///" + cwd +"/traceroute.html")




def find_lat_long(current_zip):
    #find_lat_long takes a zipcode as a parameter and uses pgeocode to 
    #find the latitude and longitude of the zipcode
    #as well as make a reference to the name of the location
    
    geolocator = Nominatim1('us')
    lat = geolocator.query_postal_code(current_zip)[-3]
    long = geolocator.query_postal_code(current_zip)[-2]
    current_data = check_db_zip(current_zip)
    
    lats.append(lat)
    longs.append(long)
    cities.append(current_data['City'])
    
    
    
def plot_centers(addresses):
    #Using geopy, a set of addresses are turned into lat and long values
    #and added to location data sets
    geolocator = Nominatim2(user_agent = "HackVioletHerHome")
    for loc in addresses:
        location = geolocator.geocode(loc)
            
        try:
            lats.append(location.latitude)
            longs.append(location.longitude)
            cities.append(loc)
        except AttributeError:
            print("Location "+ loc + ".is not formatted correctly")
            continue
            
        
         
  
def registry_website(current_zip):
    #*******Website not creted or owned******* registry_website links
    #to an external resource by City-Data.com which provides location
    #based information about the sex offender registry
    #This link is explicity used as a resource for further information
    
    site = 'http://www.city-data.com/soz/soz-'+current_zip+'.html'
    webbrowser.open(site)
    
    
def compile_map(current_zip):
    #compile_map calls functions to add data to the location datasets and 
    #then map the data
    
    find_lat_long(current_zip)
    plot_centers(check_db_address())
    plot_lat_long(lats, longs, cities)
    