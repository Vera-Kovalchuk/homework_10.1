import csv
import logging

import openpyxl

from src.utils import current_dir

PATH_TO_CSV = current_dir / "files" / "transactions.csv"
PATH_TO_EXCEL = current_dir / "files" / "transactions_excel.xlsx"

logger = logging.getLogger("files")
logger.setLevel(logging.INFO)
fileHandler = logging.FileHandler(current_dir / "logs" / "files.log", encoding="UTF-8", mode="w")
fileFormatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
fileHandler.setFormatter(fileFormatter)
logger.addHandler(fileHandler)


def read_file_csv(file):
    try:
        logger.info("Получаем данные файла")
        with open(file, "r", encoding="UTF-8") as f:
            reader = csv.DictReader(f, delimiter=";")

            filtered_data = []
            for row in reader:
                if row["id"] == "" or row["state"] == "" or row["date"] == "":
                    continue
                filtered_data.append(
                    {
                        "id": int(row["id"]),
                        "state": row["state"],
                        "date": row["date"],
                        "operationAmount": {
                            "amount": row["amount"],
                            "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                        },
                        "from": row.get("from", ""),
                        "to": row.get("to", ""),
                        "description": row["description"],
                    }
                )
            return filtered_data
    except Exception:
        logger.error("Ошибка!")
        return []


def read_excel(file):
    try:
        transactions = []
        workbook = openpyxl.load_workbook(file)
        sheet = workbook.active
        headers = [cell.value for cell in sheet[1]]

        for row in sheet.iter_rows(min_row=2, values_only=True):
            row_data = dict(zip(headers, row))
            if row_data["id"] is None or row_data["state"] is None or row_data["date"] is None:
                continue

            transactions.append(
                {
                    "id": int(row_data["id"]),
                    "state": row_data["state"],
                    "date": row_data["date"],
                    "operationAmount": {
                        "amount": row_data["amount"],
                        "currency": {"name": row_data["currency_name"], "code": row_data["currency_code"]},
                    },
                    "from": row_data.get("from", ""),
                    "to": row_data.get("to", ""),
                    "description": row_data["description"],
                }
            )
        return transactions
    except FileNotFoundError:
        print(f"Файл не найден: {file}")
        return []


if __name__ == "__main__":
    print(read_file_csv(PATH_TO_CSV))
    # print(read_excel(PATH_TO_EXCEL))