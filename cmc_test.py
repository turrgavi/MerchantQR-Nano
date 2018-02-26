from coinmarketcap import Market
coinmarketcap = Market()

data = coinmarketcap.ticker("BITCOIN", limit=3, convert="AUD")
price = data[0]['price_aud']

print(price)
