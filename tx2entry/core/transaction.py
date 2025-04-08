class Transaction:
    def __init__(self, date, tx_type, coin, amount, wallet, tx_id=None, price=None, currency="EUR"):
        self.date = date                      # Transaktionsdatum
        self.tx_type = tx_type                # Mining, Trade, Staking etc.
        self.coin = coin                      # Kryptowährung (BTC, ETH, etc.)
        self.amount = amount                  # Menge des Coins
        self.wallet = wallet                  # Quelle/Ziel (z.B. Binance)
        self.tx_id = tx_id                    # Blockchain-ID (optional)
        self.price = price                    # Bewertungspreis in Fiat
        self.currency = currency              # Zielwährung (EUR/USD etc.)
