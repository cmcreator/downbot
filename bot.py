import os.path
import telebot
import botconfig
from downloader import Downloader

bot = telebot.TeleBot(botconfig.TOKEN)

def del_folder(path):
    all_path=os.path.join(os.getcwd(),path)
    os.removedirs(all_path)


@bot.message_handler(commands=['audio'])
def echo_all(message):
    path=os.path.join(str(message.chat.id),str(message.message_id))
    user = Downloader(path=path)
    url = message.text.split(' ')[1]
    user.run(url=url)
    mp3_path = os.path.join(os.getcwd(), user.path, user.name_file)
    audio = open(mp3_path, 'rb')  # Открываем файл
    bot.send_audio(message.chat.id, audio)
    audio.close()  # Закрываем файл
    user.del_file()
    del_folder(path)

if __name__ == '__main__':
    while True:
        try:
            bot.polling()
        except Exception as exc:
            print(exc)
