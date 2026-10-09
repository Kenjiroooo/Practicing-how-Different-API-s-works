import urllib.request
import json

print("Welcome to the Currency Exchange Explorer!")
# choose your own currency
user_currency = input("Enter your main currency code (e.g., USD, EUR, PHP, JPY): ")
user_currency = user_currency.upper()

if user_currency == "":
    user_currency = "USD"

api_key = "YOUR_API_KEY_HERE" 
url = "http://api.currencylayer.com/live?access_key=" + api_key

print("Fetching data from CurrencyLayer...")
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')
