import herepy
import ast

def getLocationDetails(latitude, longitude):
    latitude = float(latitude)
    longitude = float(longitude)

    gp = herepy.GeocoderReverseApi('d6rKks8dfXLzDvHGl_mC9Q')
    response = gp.retrieve_addresses([latitude, longitude])
    response = str(response)
    response = ast.literal_eval(response)
    response = response["items"][0]["address"]["label"]

    return response

result = getLocationDetails(19.310472, 72.854042)
print(result)