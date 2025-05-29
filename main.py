import openai
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Your API keys (replace with your own)
openai.api_key = "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"
TELEGRAM_BOT_TOKEN = "8128166337:AAFDD7JG9y6uJNrsIXZHvSScap4b35AxqVA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hi! I'm your GPT bot. Ask me anything!")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response['choices'][0]['message']['content']
        await update.message.reply_text(reply)
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
