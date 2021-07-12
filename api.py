import requests

def doge():
  api = requests.get('https://sochain.com//api/v2/get_price/DOGE')
  j_api = api.json()
  name = j_api['data']['network']
  btc, usd = dict(), dict()
  for coin in j_api['data']['prices']:
    if coin['price_base'] == 'BTC' and coin['exchange'] == 'binance':
      btc['price_base'] = coin['price_base']
      btc['price'] = coin['price']
    elif coin['price_base'] == 'USD' and coin['exchange'] == 'binance':
      usd['price_base'] = coin['price_base']
      usd['price'] = coin['price']
    
  return name, btc, usd

