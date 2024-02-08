import requests
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

BASE_URL = "http://localhost:8000"
PHONE, ME = range(2)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Здравствуйте!!! Введите свой номер: /set_phone <phone>')

    return PHONE


async def set_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        due = context.args[0]
        phone = ''.join(filter(lambda x: x.isdigit(), due))
        await update.effective_message.reply_text(phone)

        profile = {
            "phone": phone,
            "username": update.message.from_user.name,
            "first_name": update.message.chat.first_name,
            "last_name": update.message.chat.last_name,
        }

        response = requests.post(f"{BASE_URL}/api/set_phone/", json=profile)
        if not response.ok:
            response_2 = requests.get(f"{BASE_URL}/api/me/{phone}")
            if update.message.from_user.name == response_2.json()["username"]:
                pass
            else:
                await update.effective_message.reply_text("этот номер занят")
                return
        context.user_data['user_phone'] = phone
        await update.effective_message.reply_text(f'Номер: {phone}!!, /me - информация о пользователе')
        return ME

    except (IndexError, ValueError):

        await update.effective_message.reply_text("Usage: /set_phone <phone> ")


async def me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phone = context.user_data['user_phone']
    response = requests.get(f"{BASE_URL}/api/me/{phone}")
    data = response.json()
    await update.message.reply_text(f"Информация о пользователе с номером: {context.user_data['user_phone']}")
    await update.message.reply_text(f"username: {data['username']}")
    await update.message.reply_text(f"Имя: {data['first_name']}")
    await update.message.reply_text(f"Фамилия: {data['last_name']}")

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "До свидания! Можно в любой момент вновь начать диалог - /start", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


application = Application.builder().token("6422745350:AAGGOyif5eV_w8eCT0FO1ny_oUGisbA3oRQ").build()

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        PHONE: [CommandHandler("set_phone", set_phone)],
        ME: [CommandHandler("me", me)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)
application.add_handler(conv_handler)

application.run_polling(allowed_updates=Update.ALL_TYPES)
