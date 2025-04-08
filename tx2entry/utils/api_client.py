import requests

class APIClient:
    BASE_URL = "https://api.coingecko.com/api/v3"

    def get_historical_price(self, coin_id, date, currency):
        endpoint = f"/coins/{coin_id}/history?date={date.strftime('%d-%m-%Y')}"
        response = requests.get(self.BASE_URL + endpoint)
        data = response.json()
        return data["market_data"]["current_price"][currency.lower()]
