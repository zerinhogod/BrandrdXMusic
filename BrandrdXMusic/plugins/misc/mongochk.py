from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
import re
from BrandrdXMusic import app as Hotty


mongo_url_pattern = re.compile(r'mongodb(?:\+srv)?:\/\/[^\s]+')


@Hotty.on_message(filters.command("mongochk"))
async def mongo_command(client, message: Message):
    if len(message.command) < 2:
        await message.reply("Por favor, insira a URL do seu MongoDB após o comando. Exemplo: /mongochk sua_url_mongodb")
        return

    mongo_url = message.command[1]
    if re.match(mongo_url_pattern, mongo_url):
        try:
            # Attempt to connect to the MongoDB instance
            client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
            client.server_info()  # Will cause an exception if connection fails
            await message.reply("A URL do MongoDB é válida e a conexão foi bem-sucedida.")
        except Exception as e:
            await message.reply(f"Failed to connect to MongoDB: {e}")
    else:
        await message.reply("Formato de URL do MongoDB inválido.")
