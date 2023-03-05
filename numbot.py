import telebot
import random
import schedule
import time

bot = telebot.TeleBot('')
chat_id = 734357667


def generate():
    num = random.randint(0, 100)
    bot.send_message(chat_id, f'{num}')


schedule.every().day.at('12:00').do(generate)
schedule.every().day.at('16:00').do(generate)

while True:
    schedule.run_pending()
    time.sleep(1)


bot.polling(non_stop=True)
