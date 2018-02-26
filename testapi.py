from coinmarketcap import Market
import json
import requests

tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

coinmarketcap = Market()
data = coinmarketcap.ticker("NANO", limit=3, convert="AUD")


price = data[0]['price_aud']
request = requests.get(tickerURL)
#data = request.json()


#price = data['price_aud']


print(price)
