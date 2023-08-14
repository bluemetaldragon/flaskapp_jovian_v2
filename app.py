import os
from flask import Flask, render_template, jsonify, request
from database import get_from_db, get_from_db_using_id,post_application_to_db



app = Flask(__name__)

@app.route("/")
def hellow():
    """renders the main page"""
    jobs = get_from_db()
    return render_template("index.html", jobs=jobs)



@app.route("/api/jobs/<id>")
def return_jobs_from_id(id):
    """renders the json object on calling /api/jobs/id page"""
    this_job = get_from_db_using_id(id)
    return render_template("jobs_page.html", job=this_job)



@app.route("/api/jobs/")
def return_jobs():
    """renders the json object on calling /api/jobs page"""
    jobs = get_from_db()
    return jsonify(jobs)



@app.route("/api/jobs/<id>/apply", methods =['post'])
def apply_to_job(id):
#    data = request.args

    #capture the posted data from the submit button into data variable
    data = request.form
    job = get_from_db_using_id(id)
#    return jsonify(data)
    status_msg = post_application_to_db(id, data)
    return render_template('submit_form_to_db.html', app_data=data, job=job, status=status_msg)


if __name__ == '__main__':
    #to avoid the error of some other process using port 5000
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port, debug=True)
    #app.run(debug=True)
