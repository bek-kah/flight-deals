import requests
import chardet

class DataManager:
    def __init__(self):
        self.endpoint = 'https://api.sheety.co/e00247fef0aed330c7d09b14d34ca934/myFlightDeals/prices'
        self.auth = {
            'Authorization': "Basic YmVra2Y6cGFzc3dvcmQ="
        }
        self.cities = []
        self.lowest_prices = []

    def city_and_prices(self):
        response = requests.get(url=self.endpoint, headers=self.auth)
        data = response.json()
        prices = data['prices']
        for price in prices:
            self.cities.append(price['city'])
            self.lowest_prices.append(price['lowestPrice'])
        return self.cities, self.lowest_prices

    def write_codes(self, codes):
        row = 2
        for code in codes:
            parameters = {
                'price': {
                    'iataCode': code
                }
            }
            req = requests.put(url=f'{self.endpoint}/{row}', json=parameters, headers=self.auth)
            row += 1
            req.raise_for_status()
