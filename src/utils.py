import json
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
    data = get_operations_metadata('C:\Users\koval\PycharmProjects\homework\data\operations.json')
