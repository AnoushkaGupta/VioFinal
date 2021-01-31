from firebase import firebase

db = firebase.FirebaseApplication('https://hackviolet2021-default-rtdb.firebaseio.com/', None)

#Tempalete for adding data to database
#data = {'City': "New York, New York",
    #     'Total Crime': 3988,
    #    'Violent Crime': 679,
    #    "Avg Property Value": 299920,
    #   "Price Sqr Ft" : 1790
    #  }

#db.put("Zipcode",10001, data)
#--------------------------------------------------------------------
def check_db_zip(input_zipcode):
    #check_db cross checks a zipcode against the database to find
    #stored information
    #If the zipcode is not stored a dictionary of data is not returned, 
    #throwing an error.
    
    dic = db.get('/Zipcode/', '')  
    for key in dic:
        if key == input_zipcode:
            print("zipcode found")
            return dic[str(key)]        
    print("zipcode not found")  
    
def check_db_address():
    dic = db.get('/Addresses/', '')
    addresses = []
 
    for key in dic:
        addresses.append(dic[key])
    return addresses

def add_address(street, city, state, country, zipcode):
    address = street +' '+ city +', '+ state+ str(zipcode)+', ' + country
    db.post('/Addresses/', address)
    
    

add_address("20 Church St.", 'Owego', 'NY', 'US', "13827")
add_address("112 State Street.", 'Albany', 'NY', 'US', "12207")
add_address('50 Haven Avenue', 'New York', 'NY', 'US', 10032)
                             
