# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup

from data.config import admins


def check_user_out_func(user_id):
    menu_default = ReplyKeyboardMarkup(resize_keyboard=True)
    menu_default.row("💙 | Купить", "💙 | Профиль", "💙 | Правила")
    menu_default.row("💙 | Поддержка", "💙 | Discord")
    if str(user_id) in admins:
        menu_default.row("💙 Управление товарами", "💙 Статистика")
        menu_default.row("💙 Настройки", "💙 Рассылка и чек", "💙 Платежные системы")
    return menu_default


all_back_to_main_default = ReplyKeyboardMarkup(resize_keyboard=True)
all_back_to_main_default.row("⬅ На главную")
