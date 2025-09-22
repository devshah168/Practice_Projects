import requests
import datetime as dt
import smtplib
import time
MY_EMAIL = "devthebeast168@gmail.com"
MY_PASSWORD = "mbvm flri fyew osql"
MY_LAT = 20.593683
MY_LNG = 78.962883


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5<=iss_latitude<=MY_LAT+5 and MY_LNG-5<=iss_longitude<=MY_LNG+5:
        return True

def is_night():
    parameters={
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted":0,
    }
    response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data=response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now=dt.datetime.now().hour
    if time_now>=sunset or time_now<=sunrise:
        return True
# print(data)
# types of response codes
# 404-not available
# 1xx- hold on
# 2xx- here you go
# 3xx-go away
# 4xx-you screwed up
# 5xx-i screwed up(server mistake)

while True:
    time.sleep(60)
    if is_iss_overhead and is_night:
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,msg="Subject:LOOK UP\n\nTHE ISS IS ABOVE YOU IN THE SKY")

