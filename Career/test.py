from urllib.request import urlopen
from bs4 import BeautifulSoup
from jobs import Jobs
import mlab
mlab.connect()

url = "https://targetjobs.co.uk/careers-advice/job-descriptions/454217-validation-engineer-job-description"
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
h1 = soup.find("h1")
job_name = h1.string.replace(": job description","")
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
    if empl_a.parent.name != "h3":
        # job_des_link_lists.remove(url)
        print("no emplh3")
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
        if qual_a.parent.name != "h3":
            # job_des_link_lists.remove(url)
            print("no qualh3")
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
            if skill_a.parent.name != "h3":
                # job_des_link_lists.remove(url)
                print("no skillh3")
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
                code = job_name.lower().replace(" ","-")
                # C. Save data to db:
                # 1. Connect to database
                
                # 2. Create Document:
                j = Jobs(job_name=job_name, job_sector="job_sector", job_define=job_define,res=res,empls=empls,quals=quals,skills=skills ,code=code)
                # 3. Save date:
                j.save()