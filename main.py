main.py
import telebot

# Вставь сюда свой токен от @BotFather
TOKEN = "8250930795:AAFi6yYcpvyy9NQQ6mGOKWvELlBNJ6-Z1kc"

# Разрешённый Telegram ID (только для тебя)
ALLOWED_USER_ID = 442255930

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: message.from_user.id == ALLOWED_USER_ID)
def handle_private(message):
    bot.send_message(message.chat.id, "Привет, Ириша! Я с тобой ❤️")

@bot.message_handler(func=lambda message: message.from_user.id != ALLOWED_USER_ID)
def deny_others(message):
    bot.send_message(message.chat.id, "Извините, у вас нет доступа к этому боту.")

print("Бот запущен")
bot.polling()
