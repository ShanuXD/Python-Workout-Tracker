import requests
from datetime import datetime

# https://www.nutritionix.com/business/api
# https://sheety.co/

nutrition_apiKey = "Your_API_Key"
nutrition_id = "Nutrition_Id"
nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/f900a3d570873cc2a851dd9ea370353e/exerciseSheet/sheet1"

GENDER = "male"
WEIGHT_KG = 55
HEIGHT_CM = 165
AGE = 22

headers = {
    "x-app-id": nutrition_id,
    "x-app-key": nutrition_apiKey,
}
exercise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutrition_endpoint, headers=headers, json=parameters)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_body = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

TOKEN = "Your_Sheety_TOKEN"

sheet_header = {
"Authorization": f"Bearer {TOKEN}"
}

sheet_response = requests.post(url=sheet_endpoint, headers=sheet_header, json=sheet_body)
print(sheet_response.text)