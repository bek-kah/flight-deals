from notification_manager import NotificationManager
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData


# Max price(s) you're willing to pay
PRICES = [500]
# IATA code for airport(s) you're going to
CITY_CODES = ['TYO']

sheets = DataManager()
flights_data = FlightData()
flights_search = FlightSearch()
notify = NotificationManager()

# cities, prices = sheets.city_and_prices()
# city_codes = flights_data.iata_codes(cities)
# sheets.write_codes(city_codes)
# flights_search.flight_prices(city_codes, prices)

flights_search.flight_prices(CITY_CODES, PRICES)