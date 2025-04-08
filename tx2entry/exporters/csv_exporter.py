import pandas as pd

class CSVExporter:
    def export_datev(self, booking_entries, file_path):
        data = []
        for entry in booking_entries:
            data.append({
                "Datum": entry.date,
                "Buchungstext": entry.description,
                "Konto Soll": entry.account_debit,
                "Konto Haben": entry.account_credit,
                "Betrag": entry.amount,
                "Währung": entry.currency,
                "Belegfeld": entry.reference
            })
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False, sep=";")
