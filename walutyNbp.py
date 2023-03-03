from datetime import datetime
from requests import get

api = "http://api.nbp.pl/api/exchangerates/tables/A/{date}/?format=json"
print("Kalkulator walut")

while True:
    try:
        date = datetime.strptime(input("Wprowadz date (RRRR-MM-DD) > "), "%Y-%m-%d")
        break
    except ValueError:
        print("Data niepoprawna")

try:
    response = get(api.format(date=f"{date:%Y-%m-%d}"))
    response.raise_for_status()  # raise exception if there was an HTTP error
    kursy = {currency["code"]: currency["mid"] for currency in response.json()[0]["rates"]}
except Exception as e:
    print("Wystapil blad przy pobieraniu kursow walut:", e)
    print(response.text)
    exit(1)

while True:
    currency = input("Wprowadz trzyliterowy kod waluty > ").upper()
    if currency in kursy.keys():
        break
    print("Waluta niepoprawna")

print(f"Kurs na dzien {date:%Y-%m-%d}: 1 {currency} = {kursy[currency]} PLN")
