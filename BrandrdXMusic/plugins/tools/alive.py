import asyncio

from BrandrdXMusic import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME

@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://te.legra.ph/file/6a28c40f0dc5966f54b17.mp4",
        caption=f"Falaaaaaaaa cuzãoooo {message.from_user.mention}!\n\nSou o {MUSIC_BOT_NAME} 😎\n\nMuito melhor que muita JBL por aí, gerencio grupos e ainda faço outras coisinhas rsrs...\n\nQualquer dúvida vem no suporte!",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="🤝SUPORTE🤝", url=f"https://t.me/COMBINADOASSISTANT_bot"
            ),
            InlineKeyboardButton(
                text="🤝SUPORTE🤝", url=f"https://t.me/COMBINADOASSISTANT_bot"
            ),
        ],
                [
            InlineKeyboardButton(
                text="🤝SUPORTE🤝", url=f"https://t.me/COMBINADOASSISTANT_bot"
            ),
                ],
                [
                    InlineKeyboardButton(
                        "FECHAR", callback_data="close"
                    )
                ],
            ]
        )
    )
