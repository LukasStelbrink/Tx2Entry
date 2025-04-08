import pandas as pd
from tx2entry.core.transaction import Transaction

class CSVImporter:
    def import_transactions(self, file_path):
        df = pd.read_csv(file_path)
        transactions = []
        for _, row in df.iterrows():
            tx = Transaction(
                date=row["date"],
                tx_type=row["type"],
                coin=row["coin"],
                amount=row["amount"],
                wallet=row["wallet"],
                tx_id=row.get("tx_id", None)
            )
            transactions.append(tx)
        return transactions
