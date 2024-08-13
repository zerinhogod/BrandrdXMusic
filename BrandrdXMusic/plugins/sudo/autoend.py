from pyrogram import filters
from pyrogram.types import Message

from BrandrdXMusic import app
from BrandrdXMusic.misc import SUDOERS
from BrandrdXMusic.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>Exemplo:</b>\n\n/autoend [enable | disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "Auto encerrar músicas ativado.\n\nO meu assistente vai sair da call após alguns minutos quando nenhum arrombado estiver lá."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("Auto encerrar músicas desativado.")
    else:
        await message.reply_text(usage)
