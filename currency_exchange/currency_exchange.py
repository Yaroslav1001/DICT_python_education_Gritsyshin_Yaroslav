import json
import requests
from pprint import pprint

user_input = input("Select currency code :>")

currency = requests.get('http://www.floatrates.com/daily/%s.json' % user_input).json()

pprint(f"Курс валюты для {user_input} - {currency['eur'] ['rate']} EUR")
pprint(f"Курс валюты {user_input} - {currency['usd']['rate']} USD")