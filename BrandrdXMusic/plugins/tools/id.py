from BrandrdXMusic import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        button = InlineKeyboardButton("FECHAR", callback_data="close")
        markup = InlineKeyboardMarkup([[button]])
        message.reply_text(
            f"ID desse otário aqui {reply.from_user.first_name} é: {reply.from_user.id}",
            reply_markup=markup
        )
    else:
        button = InlineKeyboardButton("FECHAR", callback_data="close")
        markup = InlineKeyboardMarkup([[button]])
        message.reply(
           f"O ID desse grupo é: {message.chat.id}",
           reply_markup=markup
        )
