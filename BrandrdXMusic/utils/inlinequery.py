from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="pause",
            description=f"Pausar música/vídeo atual.",
            thumb_url="https://te.legra.ph/file/fe4373a26d55df8ed04e5.png",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="resume",
            description=f"Retomar música/vídeo atual.",
            thumb_url="https://te.legra.ph/file/fe4373a26d55df8ed04e5.png",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="skip",
            description=f"Pular música/vídeo atual.",
            thumb_url="https://te.legra.ph/file/fe4373a26d55df8ed04e5.png",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="end ou stop",
            description="Limpa a fila e encerra a transmissão atual.",
            thumb_url="https://te.legra.ph/file/fe4373a26d55df8ed04e5.png",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="shuffle",
            description="Embaralhar a fila atual.",
            thumb_url="https://te.legra.ph/file/fe4373a26d55df8ed04e5.png",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="loop",
            description="enable/disable repetição de faixas.",
            thumb_url="https://te.legra.ph/file/fe4373a26d55df8ed04e5.png",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
