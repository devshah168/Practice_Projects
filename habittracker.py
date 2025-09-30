import requests
import datetime
pixela_endpoint = " https://pixe.la/v1/users"
TOKEN = ""
USERNAME=""
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsofService":"yes",
    "notMinor":"yes"
}
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
graph_params = {
    "id": "graph3",
    "name": "Coding Graph",
    "unit": "Hour",
    "type": "float",
    "color": "momiji",
}
headers={
    "X-USER-TOKEN":TOKEN,
}
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
# response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.text)

today=datetime.datetime.now()
pixela_endpoint=f"{graph_endpoint}/graph3"
pixel_params={
    "date":today.strftime("%Y%m%d"),
    "quantity":'1000',
}
response=requests.post(url=pixela_endpoint,json=pixel_params,headers=headers)
print(response.text)
