import requests
from datetime import datetime
TOKEN = ""
NUTR_ID = ""
NUTR_KEY=""
NUTR_API = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint=""
exercise_text=input("Tell me which exercises you did: ")
headers = {
    "x-app-id":NUTR_ID,
    "x-app-key":NUTR_KEY,
    }

parameters={
    "query":exercise_text,
    "weight_kg":,
    "height_cm":,
    "age":,
}
response=requests.post(url=NUTR_API,json=parameters,headers=headers)
result=response.json()


today_date=datetime.now().strftime('%d/%m/%Y')
now_time=datetime.now().strftime('%X')

for exercise in result['exercises']:
    sheet_input={
        "workout":{
            "date":today_date,
            "time":now_time,
            "exercise":exercise['name'].title(),
            "duration":exercise['duration_min'],
            "calories":exercise['nf_calories'],
        }
    }
    sheet_response=requests.post(url=sheet_endpoint,json=sheet_input,auth=('',''))
    print(sheet_response.text)
