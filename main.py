"""from flask import Flask ,render_template,jsonify
app = Flask(__name__)

JOBS=[
  {
    "id":1,
    "position":"Data engineer",
    "Location":"Noida",
    "salary":"12,00000"
  },
  {
    "id":2,
    "position":"Data scientist",
    "Location":"Mumbai",
    
  },
  {
    "id":3,
    "position":"Backend-engineer",
    "Location":"Florida",
    "salary":"22,00000"
  },
  {
    "id":4,
    "position":"Frontend-engineer",
    "Location":"remote",
    "salary":"10,00000"
  }
]
 

@app.route("/")
def hello_world():
  return render_template("home.html",
                         jobs=JOBS,
                        company_name="XYZ")


@app.route("/jobs")
def list_jobs():
  return jsonify("JOBS")
  
if __name__ == "__main__":
  app.run(host="0.0.0.0",debug =True)
"""


from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db
app = Flask(__name__)

@app.route("/")
def hello_jovian():
  jobs = load_jobs_from_db()
  return render_template('home.html', 
                         jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  
  if not job:
    return "Not Found", 404
  
  return render_template('jobpage.html', 
                         job=job)

@app.route("/api/job/<id>")
def show_job_json(id):
  job = load_job_from_db(id)
  return jsonify(job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id, data)
  return render_template('application_submitted.html', 
                         application=data,
                         job=job)



  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
