class BookingEntry:
    def __init__(self, date, description, account_debit, account_credit, amount, currency="EUR", reference=None):
        self.date = date
        self.description = description
        self.account_debit = account_debit      # Sollkonto
        self.account_credit = account_credit    # Habenkonto
        self.amount = amount
        self.currency = currency
        self.reference = reference              # z.B. Transaktions-ID
