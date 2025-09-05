import eel
import requests
# Hier importeren we de functie uit web/ml_model.py, daar waar de machine learning logica staat
from web.ml_model import train_and_predict

# Initialiseer eel met de map 'web'
# Eel is een bibliotheek die Python en JavaScript verbindt in een desktopapplicatie
eel.init('web')

# Haal eerst de juiste doelgroep op uit de CBS API
persons_url = "https://opendata.cbs.nl/ODataApi/odata/83021NED/Persoonskenmerken"
# We halen de data op met een GET-verzoek en zetten het om naar JSON-formaat. Value bevat de relevante data.
persons_data = requests.get(persons_url).json()['value']
# age_key is de leeftijdscategorie.
age_key = None
# Ga door de opgehaalde data en zoek naar de categorie "75 jaar of ouder"
for item in persons_data:
    if "75 jaar of ouder" in item.get('Title', ''):
        # Zet de titel als age_key, dit is de leeftijdscategorie die we willen analyseren
        age_key = item['Key']
        # stop de lus
        break

# Als we de leeftijdscategorie hebben gevonden, gaan we verder met het ophalen van de rookdata
typed_url = "https://opendata.cbs.nl/ODataApi/odata/83021NED/TypedDataSet"
typed_data = requests.get(typed_url).json()['value']

# Maak 2 lege lijsten voor de jaren en de percentages rokers
percentages = []
years = []
# Ga door de opgehaalde data en filter op de juiste leeftijdscategorie
for record in typed_data:
    if record.get('Persoonskenmerken') == age_key:
        # Voeg het jaar en het percentage rokers toe aan de lijsten, :4 zorgt ervoor dat we alleen het jaartal krijgen
        years.append(int(record['Perioden'][:4]))
        # Sla voor elke entry het percentage rokers op als float
        percentages.append(float(record['Rokers_1']))

# Als er data is gevonden,
if years:
    # Pak dan het laatste jaar en voorspel het percentage rokers voor het volgende jaar
    next_year = max(years) + 1
    # Dit doen we door onze eigen functie aan te roepen in ml_model.py
    prediction = train_and_predict(years, percentages, next_year)
    # Print het resultaat in de console
    print(f"Predicted percentage for {next_year}: {prediction:.2f}%")

# eel.start start de eel applicatie en opent index.html in de browser
eel.start('index.html')

