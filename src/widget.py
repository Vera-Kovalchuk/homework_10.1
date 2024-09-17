from datetime import datetime
from typing import Any
import masks


def mask_account_card(card_input: str) -> str:
    """Функция возвращает строку с замаскированным номером"""
    card_number = ""
    card_name = ""
    for el in card_input:
        if el.isdigit():
            card_number += str(el)
        else:
            card_name += str(el)
    if len(card_number) == 16:
        number_mask = masks.get_mask_card_number(card_number)
        card_mask = card_name + number_mask
        return str(card_mask)
    else:
        number_mask = masks.get_mask_account(card_number)
        card_mask = card_name + number_mask
        return str(card_mask)


print(mask_account_card("Счет 73654108430135874305"))


def get_date(user_date: str) -> str:
    """Функция которая принимает на вход строку с датой в формате
    '2024-03-11T02:26:18.671407' и возвращает строку с датой в формате
    'ДД.ММ.ГГГГ'"""
    format_date = datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = format_date.strftime("%d.%m.%Y")
    return new_date


print(get_date("2024-03-11T02:26:18.671407"))
