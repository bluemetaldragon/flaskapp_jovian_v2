#import sqlalchemy
#import pymysql
from sqlalchemy import create_engine, text



def get_from_db():
    #note'connect_string = "mysql+pymysql://username:pwd@host/database"
    connect_string = "mysql+pymysql://516ae3996bu1xn6nyc6f:pscale_pw_yBdiPHEMHW91AOU4ODP0x1aPgvZqUZ0y6ve0dxi8K0h@aws.connect.psdb.cloud/flaskapp_jovian_v2"
    engine = create_engine(
        connect_string,
        connect_args={
            "ssl": {
                "ssl_ca": "/etc/ssl/cert.pem",
            }
        }
    )

    with engine.connect() as conn:
        select_text = text("select * from jobs")
        result = conn.execute(select_text)
        # for more details on "result" check https://docs.sqlalchemy.org/en/20/core/connections.html

    result_jobs_dict = []
    for x in result.all():
        #here "x" is a list of rows returned from result, and we are converting each to dict type
        result_jobs_dict.append (dict(x._mapping))

    return result_jobs_dict




# new function to get results directly from dB using ID
def get_from_db_using_id(id_param):
    connect_string = "mysql+pymysql://516ae3996bu1xn6nyc6f:pscale_pw_yBdiPHEMHW91AOU4ODP0x1aPgvZqUZ0y6ve0dxi8K0h@aws.connect.psdb.cloud/flaskapp_jovian_v2"
    engine = create_engine(
        connect_string,
        connect_args={
            "ssl": {
                "ssl_ca": "/etc/ssl/cert.pem",
            }
        }
    )

    with engine.connect() as conn:
        select_text = text("select * from jobs where id= :val")
        result = conn.execute(select_text, {"val": id_param})
        # for more details on "result" check https://docs.sqlalchemy.org/en/20/core/connections.html
    
    #tocheck if result was null you need to use rowcount, fetch etc
    if result.rowcount !=0:    
        result_jobs_dict = []
        for x in result.all():
            result_jobs_dict.append (dict(x._mapping))

        return result_jobs_dict
    else:
        return None


# new function to post application data to DB
def post_application_to_db(id, data):
    #get handle on the DB to write
    connect_string = "mysql+pymysql://516ae3996bu1xn6nyc6f:pscale_pw_yBdiPHEMHW91AOU4ODP0x1aPgvZqUZ0y6ve0dxi8K0h@aws.connect.psdb.cloud/flaskapp_jovian_v2"
    engine = create_engine(
        connect_string,
        connect_args={
            "ssl": {
                "ssl_ca": "/etc/ssl/cert.pem",
            }
        }
    )

    #write to DB "data" based on "id"
    with engine.connect() as conn:
        select_text = text("insert into job_apps (job_id,full_name, email, url) values(:job_id, :full_name, :email, :url)")
        result = conn.execute(select_text, {"job_id": id, "full_name": data['full_name'], "email": data['email'], "url": data['url']})
        # for more details on "result" check https://docs.sqlalchemy.org/en/20/core/connections.html
    
    #tocheck if result was null you need to use rowcount, fetch etc
    if result.rowcount !=0:
        success_msg= "Congratulations, your application is posted"
        return success_msg

    else:
        return None
