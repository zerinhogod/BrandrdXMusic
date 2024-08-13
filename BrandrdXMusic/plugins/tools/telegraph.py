import os

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegraph import upload_file

from BrandrdXMusic import app


@app.on_message(filters.command(["tgm", "tgt", "telegraph", "tl"]))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "Responda uma mídia para upar no Telegraph"
        )
    try:
        text = await message.reply("Guenta aí...")

        async def progress(current, total):
            await text.edit_text(f"📥 Baixando... {current * 100 / total:.1f}%")

        try:
            local_path = await message.reply_to_message.download( progress=progress
            )
            await text.edit_text("📤 Fazendo upload para o Telegraph....")
            upload_path = upload_file(local_path)
            await text.edit_text(
                f"[LINK](https://telegra.ph{upload_path[0]})",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "LINK",
                                url=f"https://telegra.ph{upload_path[0]}",
                            )
                        ]
                    ]
                ),
            )
            try:
                os.remove(local_path)
            except Exception:
               pass
        except Exception as e:
            await text.edit_text(f"Deu errado...\n\n<i>Motivo: {e}</i>")
            try:
                os.remove(local_path)
            except Exception:
               pass
            return
    except Exception:
        pass

__HELP__ = """
**Comandos de upload no Telegraph**

Use estes comandos para fazer o upload de mídias para o Telegraph:

- `/tgm`: Faça o upload da mídia respondida para o Telegraph.
- `/tgt`: Faz a mesma coisa do comando `/tgm`.
- `/telegraph`: Faz a mesma coisa do comando `/tgm`.
- `/tl`: Faz a mesma coisa do comando `/tgm`.

**Exemplo:**
- Responda a uma foto ou vídeo com `/tgm` para fazer o upload.

**Nota:**
Você deve responder a um arquivo de mídia para que o upload funcione.
"""

__MODULE__ = "Telegraph"
