

def haversine(lat1, lon1, lat2, lon2):
    import os
    import requests  
    import math
    """Calculate the great-circle distance between two points 
    on the Earth (specified in decimal degrees) using the Haversine formula."""
    
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)

    # Haversine formula
    a = (math.sin(dLat / 2) ** 2 + 
         math.cos(lat1) * math.cos(lat2) * 
         math.sin(dLon / 2) ** 2)
    c = 2 * math.asin(math.sqrt(a))

    # Radius of earth in kilometers
    rad = 6371
    return rad * c

def delivery_location():
    import os
    import requests  
    import math
    laeLong = -0.067007  # Longitude of the delivery location
    laeLat = 51.604252   # Latitude of the delivery location

    while True:
        try:
            postcode_raw = input("What's your postcode? ")
            # API request to get postcode details
            postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode_raw}").json()
            
            # Extracting longitude and latitude from the response
            longitude = postcode_resp['result']['longitude']
            latitude = postcode_resp['result']['latitude']
            area = postcode_resp['result']['admin_district']

        except KeyError:  # For if the postcode doesn't exist
            print('Enter a valid postcode ')
            continue  # Continue to prompt the user for a valid postcode

        except requests.exceptions.RequestException as e:  # Handle network issues
            print("Error with the postcode API:", e)
            continue

        else:
            print(f"You live in {area}.\n")
            break  # Exit loop if valid postcode is entered

    # Calculate the distance
    distance = round(haversine(laeLat, laeLong, latitude, longitude), 3)
    print(f"The distance from the delivery location is {distance} km.")
    return distance

# Call the delivery_location function to test it



def delivery_fee(distance):
    if distance <= 5:
        delivery_price = 0
        print('free shipping')
    elif distance <= 15:
        delivery_price = 3
        print('delivery price is 3 pounds')
    elif distance <= 30:
        delivery_price = 5
        print('delivery price is 5 pounds')
    else:
        delivery_price = 7
        print('delivery price is 7 pounds')

    return delivery_price



def time_slot():
    slot={
        "1) Morning":"between 9:00 to 12:00",
        "2) Afternoon" :"betwen 12:00 to 4:00",
        "3) Evening": "between 4:00 to 8:00"
        }
    return slot

def choose_time_for_delivery():
    while True:
        try:
            choose=int(input("Plese enter 1/2/3 to choose the a delivery time slot: "))
            if choose not in range(1,4):
                raise TypeError
        except TypeError:
            print("Please choose from 1/2/3: ")
        else:
            if choose==1:
                print("Your items will be delivery between 9:00 to 12:00")
            elif choose==2:
                print("Your items will be delivery between betwen 12:00 to 4:00")
            else:
                print("Your items will be delivery between betwen between 4:00 to 8:00")
        break
    
    
        