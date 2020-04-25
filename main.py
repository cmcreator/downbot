import os
from pprint import pprint

import youtube_dl

#
# ydl_opts = {
#     'format': 'bestaudio/best',
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '192',
#     }],
# }
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     meta=ydl.extract_info('https://www.youtube.com/watch?v=6BuJMvpAaDA',download=True)
#
# pprint(meta)
def chek(info):
    pprint(info)


class Downloader:
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    def __init__(self):
        self.name_file=None


    def run(self,url,param=None):
        info=self._get_and_download(url)
        self.name_file=info['title']+'-'+info['id']
        print(self.name_file)
        # chek(info)


    def _get_and_download(self, url):
        with youtube_dl.YoutubeDL(Downloader.ydl_opts) as ydl:
            meta = ydl.extract_info(url, download=True)
        return meta

    def del_file(self):
        self.name_file=self.name_file+'.mp3'
        path=os.path.join(os.getcwd(),self.name_file)
        os.remove(self.name_file)



video_url=Downloader()
video_url.run(str(input('input URL:')))
video_url.del_file()

