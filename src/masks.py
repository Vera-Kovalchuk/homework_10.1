from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]} ** **** {card_number[-4:]}"
    else:
        return "Некорректный ввод данных"


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера"""
    if account_number.isdigit() and len(account_number) == 20:
        return f"**{account_number[-4:]}"
    else:
        return "Некорректный ввод данных"


print(get_mask_account("73654108430135874305"))
