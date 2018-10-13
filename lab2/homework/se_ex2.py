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
#Lọc các tiêu đề các cột trong bảng
table1 = soup.find('table',id="tblGridData")
title_lists = [""]
td1_lists = table1.find_all("td","h_t")
for td in td1_lists:
    title = td.string.replace("\r\n                    ","")
    title_lists.append(title)
# Lấy các thông số còn lại:
table2 = soup.find('table',id="tableContent")
x = table2.find('tr')

