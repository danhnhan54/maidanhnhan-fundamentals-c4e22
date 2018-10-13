from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")
# f = open("VNM.html", "wb") 
# f.write(raw_data)
# f.close()
soup = BeautifulSoup(webpage_text,"html.parser")
