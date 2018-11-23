from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "https://targetjobs.co.uk/careers-advice/job-descriptions?"

# 1.1 Open & Connect to website
conn = urlopen(url)
# 1.2 Download raw data
raw_data = conn.read()
# 1.3 Decode Data
webpage_text = raw_data.decode("utf-8")

# print(webpage_text) - check xem chuẩn chưa
# 1.4 Save text
#  w = write
#  b = binary
# Lưu data
f = open("jobname.html", "wb") 
f.write(raw_data)
f.close()
# #2.1 Convert text to soup
# soup = BeautifulSoup(webpage_text,"html.parser")
# div_content = soup.find("div","view-content")
# a_list = div_content.find_all("a")
# jobname_lists = []
# for a in a_list:
#     job_name = a.string.replace(": job description","")
#     link = "https://targetjobs.co.uk" + a["href"]
#     jobs = OrderedDict({
#         "Job": job_name,
#         "Link": link,
#     })
#     jobname_lists.append(jobs)
# pyexcel.save_as(records=jobname_lists, dest_file_name="jobname_data.xlsx")