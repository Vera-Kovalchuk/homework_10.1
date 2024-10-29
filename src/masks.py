import logging
from typing import Union

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s",
    filename="logs/masks.log",
    filemode="w",
    )
card_number_logger = logging.getLogger()
mask_account_logger = logging.getLogger()


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    card_number_logger.info("Создаем маску карты")
    if card_number.isdigit() and len(card_number) == 16:
        card_number_logger.info("Маска номера карты создана")
        return f"{card_number[:4]} {card_number[4:6]} ** **** {card_number[-4:]}"
    else:
        card_number_logger.error("Неккоректный номер карты")
        return "Некорректный ввод данных"


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера"""
    mask_account_logger.info("Создание маски номера счета")
    if account_number.isdigit() and len(account_number) == 20:
        mask_account_logger.info("Маска номера счета создана")
        return f"**{account_number[-4:]}"
    else:
        mask_account_logger.error("Некорректный ввод данных")
        return "Некорректный ввод данных"


print(get_mask_account("73654108430135874305"))
