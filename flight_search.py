from notification_manager import NotificationManager
import requests


# IATA code for where you're flying from
FLY_FROM = 'TYS'

# Dates of departures (DD/MM/YYYY)
DEPART_MIN = '02/10/2023'
DEPART_MAX = '05/10/2023'

# Dates of return (DD/MM/YYYY)
RETURN_MIN = '01/11/2023'
RETURN_MAX = '10/11/2023'

class FlightSearch:
    def __init__(self):
        self.endpoint = 'https://api.tequila.kiwi.com/v2/search'
        self.auth = {
            'apikey': 'oTL496dCZVD87J7OqVRnrPHeNC0g8ZsW'
        }
        self.body = ''
        self.link = ''
        self.notify = NotificationManager()

    def flight_prices(self, city_codes, lowest_prices):
        __ = 0
        for city_code in city_codes:
            parameters = {
                'fly_from': "ATL",
                'fly_to': "TAS",
                'date_from': DEPART_MIN,
                'date_to': DEPART_MAX,
                'return_from': RETURN_MIN,
                'return_to': RETURN_MAX,
                'curr': 'USD',
                'price_to': 500,
            }
            response = requests.get(url=self.endpoint, params=parameters, headers=self.auth)
            response.raise_for_status()
            data = response.json()
            for _ in range(0, len(data['data'])):
                price = data['data'][_]['price']
                self.link = data['data'][_]['deep_link']

                from_country = data['data'][_]['countryFrom']['code']
                to_country = data['data'][_]['countryTo']['code']

                from_city = data['data'][_]['cityFrom']
                to_city = data['data'][_]['cityTo']

                departure = data['data'][_]['local_departure']
                arrival = data['data'][_]['local_arrival']
                self.body += f'From: {from_city}, {from_country}\nTo: {to_city}, {to_country}\n' \
                             f'Price: ${price}\nDeparture: {departure}\nArrival: {arrival}\n{self.link}\n\n'
            __ += 1
        self.notify.send_email(body=self.body)

