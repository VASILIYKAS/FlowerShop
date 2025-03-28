from aiogram.types import (
    InlineKeyboardMarkup, 
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types


def get_start_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="💬 Консультация", 
            callback_data="consultation"
        )],
        [InlineKeyboardButton(
            text="📷 Посмотреть коллекцию",
            callback_data="view_collection"
        )],
        [InlineKeyboardButton(
            text="🌸 Заказать букет под желание",
            callback_data="order_bouquet"
        )],
    ])


def get_preferred_option():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="📞 По телефону", 
            callback_data="by_phone"
        )],
        [InlineKeyboardButton(
            text="💬 В чате",
            callback_data="in_chat"
        )]
    ])


def get_consultation_phone_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(
                text="Отправить номер телефона для консультации",
                request_contact=True
            )]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )


def get_order_phone_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(
                text="Отправить номер телефона для связи",
                request_contact=True
            )]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )


def get_consultation_keyboard(user_id):
    builder = InlineKeyboardBuilder()
    builder.button(
        text="📨 Ответить",
        url=f"tg://user?id={user_id}"
    )
    return builder.as_markup()


def get_theme_bouquet():
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text="🎂 День рождения",
            callback_data="occasion_birthday"
        ),
        types.InlineKeyboardButton(
            text="💍 Свадьба",
            callback_data="occasion_wedding"
        )
    )
    builder.row(
        types.InlineKeyboardButton(
            text="🏫 В школу", 
            callback_data="occasion_school"
        ),
        types.InlineKeyboardButton(
            text="🌹 Без повода",
            callback_data="occasion_no_reson"
        )
    )
    builder.row(
        types.InlineKeyboardButton(
            text="✏️ Другой повод",
            callback_data="occasion_custom"
        )
    )
    return builder.as_markup()


def get_bouquet_keyboard(
        current_index: int,
        total: int,
        occasion: str = None,
        price: str = None
):
    builder = InlineKeyboardBuilder()

    prev_data = f"prev_{current_index}"
    next_data = f"next_{current_index}"

    if price is not None:
        price_str = 'no_matter' if price == 'no_matter' else price
        prev_data += f"_{price_str}"
        next_data += f"_{price_str}"
    elif price is None:
        price = 'no_matter'
        prev_data += "_no_matter"
        next_data += "_no_matter"
    if occasion:
        prev_data += f"_{occasion}"
        next_data += f"_{occasion}"

    builder.button(
        text="◀️ Назад",
        callback_data=prev_data
    )

    builder.button(text="🛒 Заказать", callback_data=f"order_{current_index}")

    builder.button(
        text="Вперед ▶️",
        callback_data=next_data
    )

    builder.adjust(3)
    return builder.as_markup()


def get_price_keyboards(occasion: str = None):
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text="~500 руб.",
            callback_data=f"price_500_{occasion}"
        ),
        types.InlineKeyboardButton(
            text="~1000 руб.",
            callback_data=f"price_1000_{occasion}"
        )
    )
    builder.row(
        types.InlineKeyboardButton(
            text="~2000 руб.",
            callback_data=f"price_2000_{occasion}"
        ),
        types.InlineKeyboardButton(
            text="Больше.",
            callback_data=f"price_more_{occasion}"
        )
    )
    builder.row(
        types.InlineKeyboardButton(
            text="Не важно",
            callback_data=f"price_no_matter_{occasion}"
        )
    )
    return builder.as_markup()
