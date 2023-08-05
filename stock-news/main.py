import requests
import datetime as dt

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

CONFIG_PATH = "./.project_config"


## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
def get_config():
    with open(CONFIG_PATH) as file:
        configs = {}
        for line in file.readlines():
            temp_lst = line.split("=")
            configs[temp_lst[0]] = temp_lst[1]
    return configs


def get_close_stock_price_by_date(date: str):
    API_KEY = get_config()["API_KEY"]
    response = requests.get(
        f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={API_KEY}")
    response.raise_for_status()
    print(response.json())
    return float(response.json()["Time Series (Daily)"][date]["4. close"])


now_str = dt.datetime.today()
yesterday_str = (now_str - dt.timedelta(days=1)).strftime('%Y-%m-%d')
yesterday_close_price = get_close_stock_price_by_date(yesterday_str)

# TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_str = (now_str - dt.timedelta(days=2)).strftime('%Y-%m-%d')
day_before_yesterday_close_price = get_close_stock_price_by_date(day_before_yesterday_str)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

pos_dif = abs(day_before_yesterday_close_price - yesterday_close_price)

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_dif = pos_dif / yesterday_close_price * 100
print(percent_dif)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
