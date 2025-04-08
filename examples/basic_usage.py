# basic_usage.py
from tx2entry.core.transaction import Transaction
from tx2entry.core.valuation import Valuation
from tx2entry.core.entry import BookingEntry
from tx2entry.importers.csv_importer import CSVImporter
from tx2entry.exporters.csv_exporter import CSVExporter
from tx2entry.utils.api_client import APIClient
import datetime

# Transaktionen importieren
csv_importer = CSVImporter()
transactions = csv_importer.import_transactions("transaktionen.csv")

# Bewertung vorbereiten
api_client = APIClient()
valuation = Valuation(api_client)

# Transaktionen zu Buchungssätzen wandeln
entries = []
for tx in transactions:
    eur_wert = valuation.get_fiat_value(tx.coin, tx.date, tx.amount)
    entry = BookingEntry(
        date=tx.date,
        description=f"{tx.tx_type} {tx.coin}",
        account_debit="1210",   # Krypto-Bestand
        account_credit="8400",  # Erträge
        amount=eur_wert,
        currency="EUR",
        reference=tx.tx_id
    )
    entries.append(entry)

# CSV für DATEV exportieren
csv_exporter = CSVExporter()
csv_exporter.export_datev(entries, "buchungen.csv")
