import telebot

TOKEN = "तुम्हारा_बॉट_टोकन_यहाँ_डालो"
bot = telebot.TeleBot(7352876932:AAGlUSo97MehrdHzprzRgFBJkoPActvoTYU)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! मेरा नाम SpinCoin Hub Bot है! 🚀")

bot.polling()

