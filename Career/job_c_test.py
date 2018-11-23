from jobs import Jobs
import mlab

# 1. Connect to database
mlab.connect()

# 2. Prepare data
job_name = 'Test3.2'
job_sector = 'Civil and structural engineering'
job_define = 'Academic librarians are responsible for acquiring, organising, managing and distributing library resources, and ensuring that library provision meets the needs of all its users.'
res = ['selecting, developing, cataloguing and classifying library resources', "answering readers' enquiries", 'using library systems and specialist computer applications', 'management of staff, including recruitment, training and/or supervisiory duties', 'liaising with departmental academic staff, external organisations and suppliers', 'ensuring that library services meet the needs of particular groups of users (eg staff, postgraduate students, disabled students)', 'managing budgets and resources', 'supporting independent research and learning', 'developing IT facilities', 'assisting readers to use computer equipment, conduct literature searches etc', "promoting the library's resources to users"]
emps = {
        'p': ['Self-employment is uncommon; however, secondments with different institutions and fixed-term contracts are increasingly common. Flexibility regarding geographical location may be helpful for career advancement.'],
        'li': ['Universities and their academic departments', 'Research institutes', 'Public libraries', 'Higher and further education colleges', 'Professional and learned societies', 'Specialist departments within government, hospitals, and large professional firms']
        }
quals = {
        'p': ["You are eligible to become an academic librarian with any degree, but if your first qualification isn't related to information management you will need to do a postgraduate qualification with the Chartered Institute of Library and Information Professionals (CILIP).",'Some postgraduate courses require applicants to have a certain amount of relevant work experience in library or information management. This can be gained by working as a library assistant, or via a graduate training scheme (the Lisjobnet website publishes lists of training vacancies). The Arts and Humanities Research & Council may provide funding for a limited number of course places through the Professional Preparation Masters Scheme (PPM).', 'Traineeships and postgraduate course places attract strong competition, so early applications are recommended. Further vocational training and continuing professional development is necessary in all posts, leading to more senior positions and the granting of chartered and fellowship status.'],
        'li': []
        }
skills = {
        'p': ['Employers seek confident individuals with excellent organisational and interpersonal skills. Other key skills include:'],
        'li': ['strong IT skills and familiarity with the use of databases and the internet', 'teamworking and management skills', "assessment of resources and library users' needs", 'presentation and verbal communication skills', 'subject-specific knowledge or expertise in a particular function, for example ICT resources or resource ordering']
        }
code = job_name.lower().replace(" ","-")
# 3. Create document
j = Jobs(job_name=job_name, job_sector=job_sector, job_define=job_define,res=res,emps=emps,quals=quals,skills=skills ,code=code)

# 4. Save
j.save()