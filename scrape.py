import re
import requests

BUY_URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"pagination":{},"usersSearchTerm":"Windsor, ON","mapBounds":{"west":-83.20689843217166,"east":-82.80521081010134,"south":42.165594854651694,"north":42.367324095503314},"mapZoom":12,"regionSelection":[{"regionId":792741,"regionType":6}],"isMapVisible":true,"filterState":{"isAllHomes":{"value":true},"sortSelection":{"value":"globalrelevanceex"}},"isListVisible":true}&wants={"cat1":["listResults","mapResults"],"cat2":["total"]}&requestId=4'
RENT_URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"pagination":{},"usersSearchTerm":"Windsor, ON","mapBounds":{"west":-83.20689843217166,"east":-82.80521081010134,"south":42.165594854651694,"north":42.367324095503314},"mapZoom":12,"regionSelection":[{"regionId":792741,"regionType":6}],"isMapVisible":true,"filterState":{"isAllHomes":{"value":true},"isForRent":{"value":true},"isForSaleByAgent":{"value":false},"isForSaleByOwner":{"value":false},"isNewConstruction":{"value":false},"isComingSoon":{"value":false},"isAuction":{"value":false},"isForSaleForeclosure":{"value":false}},"isListVisible":true}&wants={"cat1":["listResults","mapResults"]}&requestId=3'

headers={
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

buy_response = requests.get(BUY_URL, headers=headers)
rent_response = requests.get(RENT_URL, headers=headers)

def parse_results(text):
    match = re.search('"totalResultCount":\s?(\d+)', text)
    if match:
        return match.group(1)
    else:
        return "N/A"

print({
    "buy": parse_results(buy_response.text),
    "rent": parse_results(rent_response.text)
})
