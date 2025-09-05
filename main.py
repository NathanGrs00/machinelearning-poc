import eel
import requests

eel.init('web')

url = "https://dataderden.cbs.nl/ODataApi/odata/47013NED/TypedDataSet?$top=5"

response = requests.get(url)

print(response.json())

@eel.expose
def get_number():
    return "test number"

eel.start('index.html')

