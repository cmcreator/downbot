import os.path

import telebot
import botconfig
from main import Downloader

bot = telebot.TeleBot(botconfig.TOKEN)

@bot.message_handler(commands=['audio'])
def echo_all(message):
	url=message.text.split(' ')[1]
	user=Downloader()
	user.run(url=url)
	mp3_path=os.path.join(os.getcwd(), 'music', user.name_file)
	audio=open(mp3_path,'rb') # Открываем файл
	bot.send_audio(message.chat.id, audio)
	audio.close() # Закрываем файл
	user.del_file() # Удаляем файл
# TODO решить проблему с одновременным скачиванем одинаковых файлов
bot.polling(none_stop=False, interval=0, timeout=20)