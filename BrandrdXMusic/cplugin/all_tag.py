import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
from BrandrdXMusic import app
from BrandrdXMusic.utils.branded_ban import admin_filter


SPAM_CHATS = []


@Client.on_message(
    filters.command(["all", "mention", "mentionall"], prefixes=["/", "@", ".", "#"])
    & admin_filter
)
async def tag_all_users(client, _, message):

    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "**Coloca algum texto para marcar todos porra, tipo assim:** `@all Fala cuzões!`"
        )
        return
    if replied:
        SPAM_CHATS.append(message.chat.id)
        usernum = 0
        usertxt = ""
        async for m in client.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            usernum += 5
            usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id}) "
            if usernum == 1:
                await replied.reply_text(usertxt)
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        text = message.text.split(None, 1)[1]

        SPAM_CHATS.append(message.chat.id)
        usernum = 0
        usertxt = ""
        async for m in client.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            usernum += 1
            usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id}) "
            if usernum == 5:
                await client.send_message(
                    message.chat.id,
                    f"{text}\n\n{usertxt}\n➥ Para parar de marcar a galera é só usar: /cancel",
                )
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass


@Client.on_message(
    filters.command(
        [
            "stopmention",
            "offall",
            "cancel",
            "allstop",
            "stopall",
            "cancelmention",
            "offmention",
            "mentionoff",
            "alloff",
            "cancelall",
            "allcancel",
        ],
        prefixes=["/", "@", "#"],
    )
    & admin_filter
)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
        return await message.reply_text("**Não precisava de ignorância, mas beleza, parei de marcar a turma.**")

    else:
        await message.reply_text("**Nenhum processo em andamento!**")
        return
