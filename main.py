import requests

url = "https://dataderden.cbs.nl/ODataApi/odata/47013NED/TypedDataSet?$top=5"

response = requests.get(url)

print(response.json())