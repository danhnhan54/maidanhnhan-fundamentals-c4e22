from urllib.request import urlopen
from bs4 import BeautifulSoup
from jobs import Jobs
import mlab
mlab.connect()
# A. Crawl job_link:
url1 = "https://targetjobs.co.uk/careers-advice/job-descriptions?"

# 1.1 Open & Connect to website
conn1 = urlopen(url1)
# 1.2 Download raw data
raw_data1 = conn1.read()
# 1.3 Decode Data
webpage_text1 = raw_data1.decode("utf-8")

#2.1 Convert text to soup
soup1 = BeautifulSoup(webpage_text1,"html.parser")
div_content1 = soup1.find("div","view-content")
a_list = div_content1.find_all("a")
url_lists = []
for a in a_list:
    link = "https://targetjobs.co.uk" + a["href"]
    url_lists.append(link)
url_lists.remove("https://targetjobs.co.uk/careers-advice/job-descriptions/277573-architect-job-description")
url_lists.remove("https://targetjobs.co.uk/careers-advice/job-descriptions/454431-biotechnologist-job-description")
url_lists.remove("https://targetjobs.co.uk/careers-advice/job-descriptions/278981-clinical-microbiologist-job-description")
url_lists.remove("https://targetjobs.co.uk/careers-advice/job-descriptions/278995-colour-technologist-job-description")
url_lists.remove("https://targetjobs.co.uk/careers-advice/job-descriptions/279077-community-education-officer-job-description")
url_lists.remove("https://targetjobs.co.uk/careers-advice/job-descriptions/454127-computer-scientist-job-description")
url_lists.remove("https://targetjobs.co.uk/careers-advice/job-descriptions/279123-consumer-rights-adviser-job-description")
url_lists.remove("https://targetjobs.co.uk/careers-advice/job-descriptions/279147-corporate-treasurer-job-description")
url_lists.remove("https://targetjobs.co.uk/careers-advice/job-descriptions/279155-couriertour-guide-job-description")
url_lists.remove("https://targetjobs.co.uk/careers-advice/job-descriptions/454507-crystallographer-job-description")

# B. Crawl job data:
xxx = 1
for url in url_lists:
        if xxx > 70:
                print(url)
                print("---------------------")
                # 1.1 Open & Connect to website
                conn = urlopen(url)
                # 1.2 Download raw data
                raw_data = conn.read()
                # 1.3 Decode Data
                webpage_text = raw_data.decode("utf-8")



                #2.1 Convert text to soup
                soup = BeautifulSoup(webpage_text,"html.parser")
                #2.2 Job define
                div_define = soup.find("div","field field-name-field-abstract field-type-text-long field-label-hidden")
                job_define = div_define.find("div","field-item even").string
                #2.3 Job des
                div_content = soup.find("div",property="content:encoded")
                #2.3.1 Responsibility:
                resp_ul = div_content.find("ul")
                res = []
                for li in resp_ul:
                        resp = li.string
                        if resp != '\n':
                                res.append(resp)

                # 2.3.2 Employers:
                empl_h3 = div_content.find("h3")
                tag_next = empl_h3.next_sibling
                empl_p_lists = []
                empl_li_lists = []
                empls = {
                        "p": empl_p_lists,
                        "li": empl_li_lists 
                }
                while tag_next != None and tag_next.name != "h3":
                        if tag_next.name == None:
                                tag_next=tag_next.next_sibling
                        elif tag_next.name == "p":
                                p = tag_next.string
                                if p != None:
                                        empl_p_lists.append(p)
                                tag_next=tag_next.next_sibling
                        elif tag_next.name == "ul":
                                for li in tag_next:
                                        li = li.string
                                        if li != "\n":
                                                empl_li_lists.append(li)     
                                tag_next=tag_next.next_sibling
                # 2.3.3. Qualification:
                tag_next2 = tag_next.next_sibling
                qual_p_lists = []
                qual_li_lists = []
                quals = {
                        "p": qual_p_lists,
                        "li": qual_li_lists 
                }
                while tag_next2 != None and tag_next2.name != "h3":
                        if tag_next2.name == None:
                                tag_next2=tag_next2.next_sibling
                        elif tag_next2.name == "p":
                                p = tag_next2.string
                                if p != None:
                                        qual_p_lists.append(p)
                                tag_next2=tag_next2.next_sibling
                        elif tag_next2.name == "ul":
                                for li in tag_next2:
                                        li = li.string
                                        if li != "\n":
                                                qual_li_lists.append(li)     
                                tag_next2=tag_next2.next_sibling
                # 2.3.4. Skills:
                tag_next3 = tag_next2.next_sibling
                skill_p_lists = []
                skill_li_lists = []
                skills = {
                        "p": skill_p_lists,
                        "li": skill_li_lists 
                }
                while tag_next3 != None and tag_next3.name != "h3":
                        if tag_next3.name == None:
                                tag_next3=tag_next3.next_sibling
                        elif tag_next3.name == "p":
                                p = tag_next3.string
                                if p != None:
                                        skill_p_lists.append(p)
                                tag_next3=tag_next3.next_sibling
                        elif tag_next3.name == "ul":
                                for li in tag_next3:
                                        li = li.string
                                        if li != "\n":
                                                skill_li_lists.append(li)     
                                tag_next3=tag_next3.next_sibling
                # 2.4: Job Name & Sector
                h1 = soup.find("h1")
                job_name = h1.string.replace(": job description","")
                job_sector = soup.find("ul","links top").a.string
                code = job_name.lower().replace(" ","-")
                # C. Save data to db:
                # 1. Connect to database
                
                # 2. Create Document:
                j = Jobs(job_name=job_name, job_sector=job_sector, job_define=job_define,res=res,empls=empls,quals=quals,skills=skills ,code=code)
                # 3. Save date:
                j.save()
        else:
                xxx += 1
