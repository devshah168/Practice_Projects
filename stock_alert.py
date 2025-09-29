import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
URL = "https://www.alphavantage.co/query"
NEWS_API = "https://newsapi.org/v2/everything"
URL_KEY = ""
NEWS_KEY=""
account_sid = ""
auth_token = ""
parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":URL_KEY,
    
}
parameters_news={
    "apiKey":NEWS_KEY,
    "qInTitle":COMPANY_NAME,
}


response=requests.get(url=URL,params=parameters)
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
yesterday_data=data_list[0]
yesterday_close=yesterday_data["4. close"]

day_before_yesterday=data_list[1]
day_before_yesterday_close = day_before_yesterday["4. close"]
difference = float(yesterday_close) - float(day_before_yesterday_close)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
diff_perc=round((difference/float(yesterday_close))*100)
print(diff_perc)
if abs(diff_perc)>1:
    news_response=requests.get(url=NEWS_API,params=parameters_news)  
    articles=news_response.json()["articles"]
    three_articles=articles[:3]
    article_list = [ f"{STOCK}: {up_down}{diff_perc}%\Headline: {article['title']}.\nBrief: {article['description']}"for article in three_articles]
    client = Client(account_sid, auth_token)
    for article in article_list:
        message = client.messages.create(
        from_='',   
        body=article,
        to=''
        )
    print(message.status)
