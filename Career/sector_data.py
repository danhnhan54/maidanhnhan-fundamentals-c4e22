from urllib.request import urlopen
from bs4 import BeautifulSoup

# A. Crawl job_sector:
url2 = "https://targetjobs.co.uk/career-sectors"

# 1.1 Open & Connect to website
conn2 = urlopen(url2)
# 1.2 Download raw data
raw_data2 = conn2.read()
# 1.3 Decode Data
webpage_text2 = raw_data2.decode("utf-8")

#2.1 Convert text to soup
soup2 = BeautifulSoup(webpage_text2,"html.parser")
div_sector = soup2.find("div","sectors-list margin-top margin-bottom")
a_list = div_sector.find_all("a")
sector_list = []
job_sector = {}
for a in a_list:
    sector = a.string
    job_sector = {
        "sector": sector,
        "job_name": []
    }
    sector_list.append(job_sector)
print(len(sector_list))
Accountant: job description
Accounting technician: job description
Auditor: job description
Corporate treasurer: job description
Financial manager: job description
Management accountant: job description
Tax inspector: job description