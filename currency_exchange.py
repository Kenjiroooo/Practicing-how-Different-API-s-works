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

parsed_data = json.loads(data)

if parsed_data['success'] == True:
    rates = parsed_data['quotes']
    
    usd_to_user_currency = rates.get("USD" + user_currency)
    
    if usd_to_user_currency == None:
        print("Sorry, couldn't find that currency!")
    else:
        print("\n--- Top 15 Exchange Rates (Base: " + user_currency + ") ---")
        
        count = 0
        for code in rates:
            if count == 15:
                break
                
            rate_vs_usd = rates[code]
            final_rate = rate_vs_usd / usd_to_user_currency
            
            count = count + 1
else:
    print("Uh oh, the API returned an error.")
