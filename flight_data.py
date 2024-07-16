import requests


class FlightData:
    def __init__(self):
        self.endpoint = 'https://api.tequila.kiwi.com'
        self.headers = {
            'apikey': 'oTL496dCZVD87J7OqVRnrPHeNC0g8ZsW',
        }

    def iata_codes(self, cities):
        city_codes = []
        extension = '/locations/query'
        for city in cities:
            parameter = {
                'term': city
            }
            response = requests.get(url=f'{self.endpoint}{extension}', params=parameter, headers=self.headers)
            data = response.json()
            city_code = data['locations'][0]['code']
            city_codes.append(city_code)
        return city_codes

