
import requests
from datetime import datetime

now = datetime.now()
today_date = now.strftime("%d-%m-%Y")
url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(581, today_date)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
response=requests.get(url,headers=headers)
#print(response.text)
response_json = response.json()
for center in response_json["centers"]:
    for session in center["sessions"]:
        if session["available_capacity"]>0:
            message = "Pincode: {}\n Name: {}\n State: {}\n District: {}\n Fee Type: {}\n Date: {}\n Available Capacity: {}\n Vaccine: {}\n Slots: {}\n Available Capacity Dose1: {}\n Available Capacity Dose2: {}\n Minimum Age: {}\nFor Self Registration: https://selfregistration.cowin.gov.in/".format(
            center["pincode"], center["name"],center["state_name"],center["district_name"],center["fee_type"],
            session["date"],session["available_capacity"],session["vaccine"],session["slots"],session["available_capacity_dose1"],session["available_capacity_dose2"],
            session["min_age_limit"])

            print(message)         
        
	
