import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    InputMediaVideo,
    Message,
)
from config import LOGGER_ID as LOG_GROUP_ID
from BrandrdXMusic import app
from BrandrdXMusic.utils.database import get_assistant
from BrandrdXMusic.utils.database import delete_served_chat

photo = [
    "FOTO AQUI",
    "FOTO AQUI",
    "FOTO AQUI",
    "FOTO AQUI",
    "FOTO AQUI",
]


@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    try:
        userbot = await get_assistant(message.chat.id)

        left_chat_member = message.left_chat_member
        if left_chat_member and left_chat_member.id == (await app.get_me()).id:
            remove_by = (
                message.from_user.mention if message.from_user else "Usuário desconhecido"
            )
            title = message.chat.title
            username = (
                f"@{message.chat.username}" if message.chat.username else "Grupo privado"
            )
            chat_id = message.chat.id
            left = f"<b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> \n\nGrupo: {title}\n\nID do group: {chat_id}\n\nRemovido por: {remove_by}\n\nBOT: @{app.username}"
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
            await delete_served_chat(chat_id)
            await userbot.leave_chat(chat_id)
    except Exception as e:
        return
