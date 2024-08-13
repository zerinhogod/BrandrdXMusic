from pyrogram.enums import ParseMode

from BrandrdXMusic import app
from BrandrdXMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} log de músicas</b>

<b>ID do grupo:</b> <code>{message.chat.id}</code>
<b>Nome do grupo:</b> {message.chat.title}
<b>Usuário do grupo:</b> @{message.chat.username}

<b>ID do usuário:</b> <code>{message.from_user.id}</code>
<b>Nome:</b> {message.from_user.mention}
<b>Username:</b> @{message.from_user.username}

<b>Consulta:</b> {message.text.split(None, 1)[1]}
<b>Tipo de stream:</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
