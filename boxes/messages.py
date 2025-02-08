from typing import Optional

from settings import MASTER_USERNAME


def choice_delivery_text() -> str:
    return "Супер! Отправляю по всей России, а из Санкт-Петербурга можно также забрать самовывозом, метро Проспект Просвещения (если ты из спб и удобнее доставкой – выбирай ее)"

def box_info_text(price: int) -> str:
    if price == 1990:
        size = "маленький"
    elif price == 2990:
        size = "средний"
    else:
        size = "большой"

    return f"На фото показано то что идет в каждый <i>{size}</i> бокс, остальные несколько позиций можно будет выбрать из разных вариантов ❄️"


def user_info_text() -> str:
    return (
        "<b>Теперь укажи данные для доставки:</b>\n"
        "1. ФИО\n"
        "2. Номер телефона\n"
        "3. Адрес пункта СДЭК\n"
        "4. Электронная почта (туда придет трек-номер отслеживания)"
    )


def final_text(username: Optional[str] = None) -> str:
    return (
        "Готово! Поздравляю с покупкой, ты самый быстрый котенок 🦔🤍\n\n"
        "Скоро я свяжусь с тобой для оплаты и уточнения деталей 🎀"
        if username
        else "Готово! Спасибо за заказ, но, кажется, у вас не указан юзернэйм и я не смогу с вами связаться :(\n"
        f"Напишите пожалуйста мне в лс для оплаты и уточнения деталей 🧸❤️\n\n Аккаунт: {MASTER_USERNAME}"
    )


def order_text(
    username: str,
    user_info: str | None = None
) -> str:
    text = (
        "<u><b>НОВАЯ ЗАЯВКА</b></u>\n\n"
        f"<b>Информация о доставке:</b>\n{user_info if user_info else 'Самовывоз'}\n\n"
    )

    text = (
        text + f"Ссылка: https://t.me/{username}"
        if username
        else text + "У пользователя нет юзернейма, МДА УЖ 21 век на дворе"
    )

    return text
