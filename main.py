import os
import re
from pprint import pprint

import youtube_dl


class Downloader:
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',

        }],
        'outtmpl': '%(title)s-%(id)s.%(ext)s',
    }

    def __init__(self):
        self.name_file = None

    def run(self, url, param=None):
        info = self._get_and_download(url)
        self.name_file = info['title'] + '-' + info['id'] + '.mp3'
        self.refacor()


    def refacor(self):
        '''
                        Убираем ? символ из .mp3
        '''
        reg = re.compile('[?]')
        self.name_file=reg.sub('', self.name_file)



    def _get_and_download(self, url):
        '''
                Скачивание .mp3 и получение метаданных
        '''
        with youtube_dl.YoutubeDL(Downloader.ydl_opts) as ydl:
            meta = ydl.extract_info(url, download=True)
        return meta

    def del_file(self):
        '''
        Удаление .mp3
        '''
        path = os.path.join(os.getcwd(), self.name_file)
        os.remove(self.name_file)


video_url = Downloader()
video_url.run(str(input('input URL:')))
# video_url.del_file()
