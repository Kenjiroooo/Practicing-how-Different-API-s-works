import urllib.request
import json

print("Welcome to the Currency Exchange Explorer!")
# choose your own currency
user_currency = input("Enter your main currency code (e.g., USD, EUR, PHP, JPY): ")
user_currency = user_currency.upper()
