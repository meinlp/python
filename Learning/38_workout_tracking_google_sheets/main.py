# https://developer.nutritionix.com/

from dotenv import load_dotenv
from pprint import pprint
import os
import requests

load_dotenv()
APP_ID = os.getenv('NUTRITIONIX_APP_ID')
API_KEY = os.getenv('NUTRITIONIX_API_KEY')
BASE_URL = "https://trackapi.nutritionix.com/v2"
GENDER = "male"
WEIGHT = "80"
HEIGHT = '170'
AGE = '37'

url = f'{BASE_URL}/natural/exercise'
# workout = input('What did you do on your workout?\n')
workout = '20 min cardio 30min free weight'


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}
payload = {
    "query": workout,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}
result = requests.post(url=url, json=payload, headers=headers)
print(pprint(result.json()))
