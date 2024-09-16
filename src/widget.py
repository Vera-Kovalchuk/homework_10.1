from datetime import datetime

from src.masks import get_mask_card_number


def mask_account_card(card_data: str) -> str:
    """Функция возвращает строку с замаскированным номером"""
    card_number = "".join(el if el.isdigit() else "" for el in card_data)
    card_number_mask = get_mask_card_number(card_number)
    name_card = "".join("" if el.isdigit() else el for el in card_data)
    card_data_mask = name_card + card_number_mask
    return card_data_mask


print(mask_account_card("Maestro 1596837868705199"))


def get_date(user_date: str) -> str:
    """Функция которая принимает на вход строку с датой в формате
    '2024-03-11T02:26:18.671407' и возвращает строку с датой в формате
    'ДД.ММ.ГГГГ'"""
    format_date = datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = format_date.strftime("%d.%m.%Y")
    return new_date


print(get_date("2024-03-11T02:26:18.671407"))
