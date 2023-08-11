from flask import Flask, render_template, jsonify


app = Flask(__name__)

jobs = [
  {'id':1, 'title':"Sr Dev", 'loc':"Singapore", 'sal':'120k SGD'},
  {'id':2, 'title':"Jr Dev", 'loc':"Singapore"},
  {'id':3, 'title':"Sr Mgr", 'loc':"Singapore", 'sal':'150k SGD'},
]




@app.route("/")
def hellow():
    return render_template("index.html", jobs=jobs)


@app.route("/api/jobs/")
def return_jobs():
    return jsonify(jobs)




if __name__ == '__main__':
    app.run(debug=True)
