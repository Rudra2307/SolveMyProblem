import herepy
import ast
from herepy.here_api import HEREApi
from herepy.utils import Utils
from herepy.error import HEREError
from herepy.models import GeocoderReverseResponse
import json
  
def getLocationDetails(latitude, longitude):
    latitude = float(latitude)
    longitude = float(longitude)

    gp = herepy.GeocoderReverseApi('jHffeGfyLsxEo6Jn0G77H70R8mO9BXL6xQQgrJlqe4o')

    
    response = gp.retrieve_addresses([latitude, longitude])
    response = response.as_json_string()
    response = json.loads(response)
    response = response["items"][0]["address"]["label"]
    return response

# result = getLocationDetails(19.310472, 72.854042)


result = getLocationDetails(19.3919, 72.8397)
print(result)
# print(result)