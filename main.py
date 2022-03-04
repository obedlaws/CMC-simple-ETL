from wsgiref import headers
import requests
import config 
from load import LoadPipeline

apiKey = config.api_key

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': apiKey,
}

r = requests.get(url, headers=headers).json()

#print(r.status_code) // TEST IF API IS WORKING CORRECTLY


#LISTING THE WAYS TO QUERY THE JSON FILES

#names = r['data'][i]['name']
#symbols = r['data'][i]['symbol']
#first_historical_data = r['data'][i]['platform'] and ['name'] if its not None
#token_address = r['data'][i]['platform'] and ['token_address'] if its not None


#LISTS CONTAINING THE QUERIED DATA
name = []
symbols = []
platform = []
token_address = []

#GENERATE LIST OF NAMES OF TOKENS
def namesGen(list):
    i = 0

    while i < len(r['data']):
        list.append(r['data'][i]['name'])
        i += 1
        
#GENERATE LIST OF SYMBOLS OF TOKENS
def symbolsGen(list):
    i = 0

    while i < len(r['data']):
        list.append(r['data'][i]['symbol'])
        i += 1

#GENERATE LIST OF THE TOKEN PLATFORM
def platformGen(list):
    i = 0

    while i < len(r['data']):
        if r['data'][i]['platform'] == None:
            list.insert(i, 'None')
        else:
            list.append(r['data'][i]['platform']['name'])
        i += 1

#GENERATE LIST OF TOKEN ADDRESS IF AVAILABLE
def tokenAddressGen(list):
    i = 0

    while i < len(r['data']):
        if r['data'][i]['platform'] == None:
            list.insert(i, 'None')
        else:
            list.append(r['data'][i]['platform']['token_address'])
        i += 1


#PUTTING IT ALL TOGETHER!

print("Extracting...")

print("Transforming...")
namesGen(name)
symbolsGen(symbols)
platformGen(platform)
tokenAddressGen(token_address)

print('Loading...')
L = LoadPipeline()
L.create_table()
L.insert(name, symbols, platform, token_address)

print("...Done!")

print("Getting Table")
L.get_table()