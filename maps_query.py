# For google maps - location validation
import googlemaps
maps_key = "enterYourKeyHere"
gmaps_client = googlemaps.Client(key=maps_key)

# Hit Google Places API and see if it returns a valid result
geocode_result = gmaps_client.geocode(entity.name)
# print(geocode_result)
if len(geocode_result) > 0:
    # get coordinates of the location
    lat = geocode_result[0]['geometry']['location']['lat']
    long = geocode_result[0]['geometry']['location']['lng']
