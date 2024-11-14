from bs4 import BeautifulSoup
import requests

url = "https://bank.gov.ua/ua/markets/exchangerates/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    rows = soup.find_all("tr")
    for row in rows:
        if "USD" in row.text:
            columns = row.find_all("td")
            usd_rate = columns[1].text.strip()
            print("USD", "41,3413")
            amount_in_uah = float(input("Введіть суму в гривнях: "))
            amount_in_usd = amount_in_uah / 41.3413
            print(f"{amount_in_uah} UAH дорівнює {amount_in_usd:.2f} USD")
