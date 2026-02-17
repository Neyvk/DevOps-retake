import os
import telebot

bot_token = os.environ.get("BOT_TOKEN")
chat_id = os.environ.get("CHAT_ID")
bot = telebot.TeleBot(bot_token)

bot.send_message(chat_id, "бебебубу")