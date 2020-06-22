import os
import re
from pprint import pprint
import youtube_dl
import logging.config
from logconfig import dictLogConfig

logging.config.dictConfig(dictLogConfig)
logger = logging.getLogger("Youtube")


class DownloadError(Exception):
    def __init__(self):
        self.txt = 'Ошибка при скачивании'


class Downloader:
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',

        }],
        'outtmpl': '\%(title)s-%(id)s.%(ext)s',
        'noplaylist': True,
        'cachedir': False,
    }

    def __init__(self, path='music'):
        self.name_file = None
        self.path = path
        self.ydl_opts_user = self.user_param(path)

    def user_param(self, path):
        '''
            Изменение пути скачивания
        '''
        ydl_opts_user = Downloader.ydl_opts.copy()
        key, value = 'outtmpl', path + ydl_opts_user['outtmpl']
        ydl_opts_user.update({key: value})
        return ydl_opts_user

    def run(self, url):
        logger.info('Начинает работу')
        try:
            info = self._get_and_download(url)
            self.get_name(info=info)
        except Exception as exc:
            logger.exception(f'Неудалось скачать {url}')
            # raise DownloadError

    def get_name(self, info):
        '''
                        Имя файла
                        Убираем ? символ из .mp3
        '''
        self.name_file = info['title'] + '-' + info['id'] + '.mp3'
        reg = re.compile('[?]')
        self.name_file = reg.sub('', self.name_file)

    def _get_and_download(self, url):
        '''
                Скачивание .mp3 и получение метаданных
        '''
        logger.info('Скачивание mp3')
        with youtube_dl.YoutubeDL(self.ydl_opts_user) as ydl:
            meta = ydl.extract_info(url, download=True)
        logger.info('Скачало mp3 ' + meta['id'])
        return meta

    def del_file(self):
        '''
        Удаление .mp3
        '''
        logger.info(f'Удаляем {self.name_file}')
        path = os.path.join(os.getcwd(), self.path, self.name_file)
        os.remove(path)


if __name__ == '__main__':
    video_url = Downloader()
    url = str(input('input URL:'))
    video_url.run(url=url)
    # video_url.del_file()
