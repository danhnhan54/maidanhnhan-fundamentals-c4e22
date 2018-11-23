from urllib.request import urlopen
from bs4 import BeautifulSoup
from jobs import Jobs,Job_sector
import mlab
mlab.connect()
# A. Crawl job_link:
url1 = "https://targetjobs.co.uk/career-sectors"

# 1.1 Open & Connect to website
conn1 = urlopen(url1)
# 1.2 Download raw data
raw_data1 = conn1.read()
# 1.3 Decode Data
webpage_text1 = raw_data1.decode("utf-8")

#2.1 Convert text to soup
soup1 = BeautifulSoup(webpage_text1,"html.parser")
div_content1 = soup1.find("div","sectors-list margin-top margin-bottom")
a_list = div_content1.find_all("a")
sector_list = []
for a in a_list:
        sector_link = "https://targetjobs.co.uk" + a['href'] +'/advice'
        sector = {
                "job_sector": a.string,
                "sector_link": sector_link
        }
        sector_list.append(sector)
m = 1
for sector in sector_list:
    # print(sector)
    job_sector = sector['job_sector']
    js_code = job_sector.lower().replace(',','').replace(' ','-')
    js = Job_sector(job_sector=job_sector,js_code = js_code)
    js.save()
# A. Crawl job_link:
    # 1.1 Open & Connect to website
    conn2 = urlopen(sector['sector_link'])
    # 1.2 Download raw data
    raw_data2 = conn2.read()
    # 1.3 Decode Data
    webpage_text2 = raw_data2.decode("utf-8")
    #2.1 Convert text to soup
    soup2 = BeautifulSoup(webpage_text2,"html.parser")
    div_lists = soup2.find_all("div","clearfix")
    for div in div_lists:
        h3 = div.find("h3",string='Job descriptions')
        if h3 != None:
            div_job = div
    h4_lists = div_job.find_all("h4")
    job_des_link_lists = []
    for h4 in h4_lists:
        # job_name = h4.a.string.replace(": job description","")
        job_des_link = "https://targetjobs.co.uk" + h4.a['href']
        job_des_link_lists.append(job_des_link)
    n = 1
    print(m,job_sector)
    m += 1
    print("----------------------------")    
    for url in job_des_link_lists:
        if url == "https://targetjobs.co.uk/careers-advice/job-descriptions/277573-architect-job-description":
                job_des_link_lists.remove("https://targetjobs.co.uk/careers-advice/job-descriptions/277573-architect-job-description")
        else:
                print(n)
                print(url)
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
                if resp_ul != None:
                        res = []
                        for li in resp_ul:
                                resp = li.string
                                if resp != '\n':
                                        res.append(resp)

                        # 2.3.2 Employers:
                        empl_a = div_content.find("a",attrs={"name":"employers"})
                        if empl_a == None:
                                job_des_link_lists.remove(url)
                                n +=1
                        elif empl_a.parent.name != "h3":
                                job_des_link_lists.remove(url)
                                n +=1
                        elif empl_a.parent.name == "h3":
                                empl_h3 = empl_a.parent
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
                                qual_a = div_content.find("a",attrs={"name":"training"})
                                if qual_a == None:
                                        job_des_link_lists.remove(url)
                                        n +=1
                                elif qual_a.parent.name != "h3":
                                        job_des_link_lists.remove(url)
                                        n +=1
                                elif qual_a.parent.name == "h3":
                                        qual_h3 = qual_a.parent        
                                        tag_next2 = qual_h3.next_sibling
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
                                        skill_a = div_content.find("a",attrs={"name":"skills"})
                                        if skill_a == None:
                                                job_des_link_lists.remove(url)
                                                n +=1
                                        elif skill_a.parent.name != "h3":
                                                job_des_link_lists.remove(url)
                                                n+=1
                                        elif skill_a.parent.name == "h3":
                                                skill_h3 = skill_a.parent
                                                tag_next3 = skill_h3.next_sibling
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
                                                code = job_name.lower().replace(" ","-").replace('/','-')
                                                print("good url")
                                                # C. Save data to db:
                                                # 1. Connect to database
                                                
                                                # 2. Create Document:
                                                j = Jobs(job_name=job_name, job_sector=job_sector, job_define=job_define,res=res,empls=empls,quals=quals,skills=skills ,code=code)
                                                # # 3. Save date:
                                                j.save()
                                                n+=1
                print("***************")