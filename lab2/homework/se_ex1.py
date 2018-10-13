from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")
# f = open("itune.html", "wb") 
# f.write(raw_data)
# f.close()
soup = BeautifulSoup(webpage_text,"html.parser")
sec = soup.find("section","section chart-grid")
topsong_lists = []
li_list = sec.find_all("li")
for li in li_list:
    stt = li.strong.string
    songname = li.h3.a.string
    artist = li.h4.a.string
    song = OrderedDict({
        'Stt': stt,
        'Song': songname,
        'Artist': artist,
    })
    topsong_lists.append(song)

pyexcel.save_as(records=topsong_lists, dest_file_name="topsong.xlsx")
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
for i in range(100):
    options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download([topsong_lists[i]['Song'] + " " + topsong_lists[i]['Artist']])