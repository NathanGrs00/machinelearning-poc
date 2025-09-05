import eel
import requests
from web.ml_model import predict_value

eel.init('web')

url = "https://opendata.cbs.nl/ODataApi/odata/83021NED/UntypedDataSet"
response = requests.get(url)

result = predict_value(6)
print("Prediction:", result)

eel.start('index.html')

