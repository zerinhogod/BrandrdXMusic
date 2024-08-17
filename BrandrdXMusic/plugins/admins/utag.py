import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
from BrandrdXMusic import app
from BrandrdXMusic.utils.branded_ban import admin_filter

SPAM_CHATS = {}


@app.on_message(
    filters.command(["utag", "uall"], prefixes=["/", "@", ".", "#"]) & admin_filter
)
async def tag_all_users(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id
    if len(message.text.split()) == 1:
        await message.reply_text(
            "**Coloca algum texto para marcar todos porra, tipo assim:** `@utag Salve seus arrombados, tomanocu geral!`"
        )
        return

    text = message.text.split(None, 1)[1]
    if text:
        await message.reply_text(
            "**Tagueamento ilimitado iniciado com sucesso!**\n\n**Tagueamento com intervalo de 7 segundos.**\n\n**➥ Desligar o tagueamento com o comando /stoputag**"
        )

    SPAM_CHATS[chat_id] = True
    f = True
    while f:
        if SPAM_CHATS.get(chat_id) == False:
            await message.reply_text("**Não precisava de ignorância, mas beleza, parei de marcar a turma.**")
            break
        usernum = 0
        usertxt = ""
        try:
            async for m in app.get_chat_members(message.chat.id):
                if m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id}), "
                if usernum == 5:
                    await app.send_message(
                        message.chat.id,
                        f"{text}\n\n{usertxt}\n➥ Desligar tagueamento por: /stoputag",
                    )
                    usernum = 0
                    usertxt = ""
                    await asyncio.sleep(7)
        except Exception as e:
            print(e)


@app.on_message(
    filters.command(
        ["stoputag", "stopuall", "offutag", "offuall", "utagoff", "ualloff"],
        prefixes=["/", ".", "@", "#"],
    )
    & admin_filter
)
async def stop_tagging(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id
    if SPAM_CHATS.get(chat_id) == True:
        SPAM_CHATS[chat_id] = False
        return await message.reply_text("**Por favor, aguarde, parando o tagueamento ilimitado...**")
    else:
        await message.reply_text("**O processo de tagueamento ilimitado não está ativo.**")
