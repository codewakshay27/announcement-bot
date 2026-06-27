import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = "8829405193:AAHRsQGk_3CBUWkXVyu6M1LXEpftEW2-kuE"

STUDENT_GROUP_ID = -1004308812014
ADMIN_GROUP_ID = -5592669200

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != ADMIN_GROUP_ID:
        return

    if update.message.text:
        await context.bot.send_message(
            chat_id=STUDENT_GROUP_ID,
            text=update.message.text
        )

    elif update.message.photo:
        await context.bot.send_photo(
            chat_id=STUDENT_GROUP_ID,
            photo=update.message.photo[-1].file_id,
            caption=update.message.caption or ""
        )

    elif update.message.document:
        await context.bot.send_document(
            chat_id=STUDENT_GROUP_ID,
            document=update.message.document.file_id,
            caption=update.message.caption or ""
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(
    MessageHandler(filters.ALL, forward_message)
)

app.run_polling()