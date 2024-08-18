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
from BrandrdXMusic.core.userbot import Userbot
from BrandrdXMusic.utils.database import delete_served_chat
from BrandrdXMusic.utils.database import get_assistant


photo = [
    "https://te.legra.ph/file/fe4373a26d55df8ed04e5.png",
    "https://te.legra.ph/file/fe4373a26d55df8ed04e5.png",
    "https://te.legra.ph/file/fe4373a26d55df8ed04e5.png",
    "https://te.legra.ph/file/fe4373a26d55df8ed04e5.png",
    "https://te.legra.ph/file/fe4373a26d55df8ed04e5.png",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = (
                    message.chat.username if message.chat.username else "Grupo privado"
                )
                msg = (
                    f"**BOT adicionado em #𝐍ᴇᴡ_𝐆ʀᴏᴜᴘ**\n\n"
                    f"**Nome do grupo:** {message.chat.title}\n"
                    f"**ID do grupo:** {message.chat.id}\n"
                    f"**Acesso ao grupo:** @{username}\n"
                    f"**Membros:** {count}\n"
                    f"**Adicionado por:** {message.from_user.mention}"
                )
                await app.send_photo(
                    LOG_GROUP_ID,
                    photo=random.choice(photo),
                    caption=msg,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    f"Perfil de quem adicionou",
                                    url=f"tg://openmessage?user_id={message.from_user.id}",
                                )
                            ]
                        ]
                    ),
                )
                await userbot.join_chat(f"{username}")
    except Exception as e:
        print(f"Error: {e}")
