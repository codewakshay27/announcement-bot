import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
STUDENT_GROUP_ID = int(os.getenv("STUDENT_GROUP_ID"))
ADMIN_GROUP_ID = int(os.getenv("ADMIN_GROUP_ID"))

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
