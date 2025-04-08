class Valuation:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_fiat_value(self, coin, date, amount, currency="EUR"):
        # API-Aufruf zur Preisermittlung via CoinGecko, etc.
        price = self.api_client.get_historical_price(coin, date, currency)
        return amount * price
