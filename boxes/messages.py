from typing import Optional

from settings import MASTER_USERNAME


def box_info_text() -> str:
    return "На фото показано то что идет в <i>каждый</i> бокс, остальные позиции можно будет выбрать из нескольких вариантов 🍂"


def user_info_text() -> str:
    return (
        "Отлично! Твой бокс составлен 🍁\n\n"
        "<b>Теперь укажи данные для доставки:</b>\n"
        "1. ФИО\n"
        "2. Номер телефона\n"
        "3. Адрес пункта выдачи Яндекс Маркет\n\n"
        "<i>*если в твоем городе нет яндекса, напиши адрес и индекс почты</i>"
    )


def final_text(username: Optional[str] = None) -> str:
    return (
        "Готово! Спасибо за заказ, скоро я свяжусь с вами для оплаты и уточнения деталей 🦔🧡"
        if username
        else "Готово! Спасибо за заказ, но, кажется, у вас не указан юзернэйм и я не смогу с вами связаться :(\n"
        f"Напишите пожалуйста мне в лс для оплаты и уточнения деталей 🦔🧡\n\n Ссылка: https://t.me/{MASTER_USERNAME}"
    )


def order_text(
    box_price: int,
    card: str,
    hedgehog_card: str,
    stickers_color: str,
    tea: str,
    chocolate: str,
    candle: str,
    user_info: str,
    magnet: Optional[str] = None,
    shopper: Optional[str] = None,
    username: Optional[str] = None,
) -> str:
    text = (
        "<u><b>НОВАЯ ЗАЯВКА</b></u>\n\n"
        f"Цена бокса: {box_price}\n\n"
        "<b>Содержимое:</b>\n"
        f"1. Открытка {card}\n"
        f"2. Надпись на открытке с Тимошей - {hedgehog_card}\n"
        f"3. Расцветка стикеров с котами - {stickers_color}\n"
        f"4. Чай {tea}\n"
        f"5. Шоколад {chocolate}\n"
        f"6. Свеча {candle}\n"
    )

    if box_price > 1990:
        text = text + f"7. Магнит {magnet}\n"

    if box_price > 2990:
        text = text + f"8. Шоппер {shopper}\n"

    text = text + "\n" + f"<b>Информация о доставке:</b>\n{user_info}\n\n"

    text = (
        text + f"Ссылка: https://t.me/{username}"
        if username
        else "У пользователя нет юзернейма, МДА УЖ 21 век на дворе"
    )

    return text
