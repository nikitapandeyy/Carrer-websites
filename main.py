from flask import Flask ,render_template,jsonify
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


