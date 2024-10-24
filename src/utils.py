import json
import os
from json import JSONDecodeError
from typing import Any


def get_operations_metadata(file_path: str) -> Any:
    """Обрабатывает JSON-файл, принимает путь к файлу в качестве аргумента"""
    empty_metadata = []
    try:
        with open(file_path, 'r', encoding='utf=8') as file:
            try:
                operations = json.load(file)
                if len(operations) == 0 or type(operations) is not list:
                    return empty_metadata
                else:
                    return operations
            except json.JSONDecodeError:
                print('Возникла ошибка при декодировании JSON-файла')
                return empty_metadata
    except FileNotFoundError:
        print('Файл не найден!')
        return empty_metadata


if __name__ == '__main__':
    #data = get_operations_metadata('C:\Users\koval\PycharmProjects\homework\data\operations.json')
    data = os.path.join(os.path.dirname(__file__), "data", "operations.json")


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
    else:
        amount = currency_conversion(trans)
    return amount