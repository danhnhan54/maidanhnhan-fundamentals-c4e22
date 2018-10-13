# 1. Download page
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "https://www.apple.com/itunes/charts/songs/"

# 1.1 Open & Connect to website
conn = urlopen(url)
# 1.2 Download raw data
raw_data = conn.read()
# 1.3 Decode Data
webpage_text = raw_data.decode("utf-8")

f = open("itunes.html", "wb") 
f.write(raw_data)
f.close()

soup = BeautifulSoup(webpage_text,"html.parser")
# 1.4 Save text
 # w = write
 # b = binary
# Lưu data
# f = open("dantri.html", "wb") 
# f.write(raw_data)
# f.close()
# 2. Extract ROI
# html: tag; value/string/content; attribute; children/sibling
#2.1 Convert text to soup
# soup = BeautifulSoup(webpage_text,"html.parser")
# ul = soup.find("ul","ul1 ulnew") # chỉ tìm giá trị đầu tiên
# news_lists = []
# li_list = ul.find_all("li")
# for li in li_list:
#     h4 = li.h4
#     a = h4.a
#     # hoặc: a = li.h4.a
#     title = a.string
#     link = url + a["href"]
#     # print(title)
#     # print(link)
#     news = OrderedDict({
#         "Title": title,
#         "Link": link,
#     })
#     news_lists.append(news)
# # print(*news_lists,sep="\n")
# pyexcel.save_as(records=news_lists, dest_file_name="hotnews.xlsx")
# # print(soup.prettify()) - sẽ thấy các đoạn code dịch vào
# # 3. Extract Data



# # 4. Save Data