from flask import *
import mlab
from jobs import Jobs,Job_sector

app = Flask(__name__)
mlab.connect()
@app.route('/personality_types')
def home():
    return render_template("personality_types.html")

@app.route('/job_sector')
def job_descriptions():
  job_sector = Job_sector.objects()
  # job_sector = [] 
  # for sector in job_sector:
  #   code = sector['job_sector'].lower()
  #   js_code = code.replace(" ","-")
  #   sector2 ={
  #     'job_sector': sector['job_sector'],
  #     'js_code': js_code
  #   }
  #   job_sector.append(sector2)
  return render_template("job_sector.html",js=job_sector)
  

@app.route('/job_sector/<js_code>')
def jobs_list(js_code):
  sector = Job_sector.objects(js_code=js_code)
  job_sector = str(sector[0]['job_sector'])
  print(job_sector,type(job_sector))
  jobs_list = Jobs.objects(job_sector=job_sector)
  return render_template("jobs_list.html",j_list=jobs_list,js_code=js_code)


@app.route('/job_sector/<js_code>/<code>')
def jobs(js_code,code):
  sector = Job_sector.objects(js_code=js_code)
  js_code = sector[0]['js_code']
  jobs_list = Jobs.objects(code=code)
  jobs = jobs_list[0]
  return render_template("job-descriptions.html", j = jobs)



if __name__ == '__main__':
  app.run(debug=True)