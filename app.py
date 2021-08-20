# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
# import other libraries 
from pymongo import MongoClient
import os
import sys
import subprocess
try:
  import pandas as pd
  from flask_cors import CORS
  import sqlalchemy
  from sqlalchemy.ext.automap import automap_base
  from sqlalchemy.orm import Session
  from sqlalchemy import create_engine
  import psycopg2
except ImportError:
  subprocess.check_call([sys.executable, '-m', 'pip','install', 'pandas'])
  subprocess.check_call([sys.executable, '-m', 'pip','install', 'flask_cors'])
  subprocess.check_call([sys.executable, '-m', 'pip','install', 'sqlalchemy'])
  subprocess.check_call([sys.executable, '-m', 'pip','install', 'psycopg2'])
finally:
  import pandas as pd
  from flask_cors import CORS
  import sqlalchemy
  from sqlalchemy.ext.automap import automap_base
  from sqlalchemy.orm import Session
  from sqlalchemy import create_engine
  import psycopg2
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
engine = create_engine("postgresql://postgres:postgres@localhost/crimes") or "sqlite:///db.sqlite"
Base = automap_base()
Base.prepare(engine, reflect=True)
#################################################
#from flask_sqlalchemy import SQLAlchemy
###!!app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
###!!app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
###!!db = SQLAlchemy(app)
###!!from .models import Pet

#################################################
# Flask Routes
# List all routes that are available.
#################################################

# Query the database and send the jsonified results
#@app.route("/send", methods=["GET", "POST"])
#def send():




    ######  

@app.route('/sqldata',methods=['GET'])
def data_ml():

    # Find one record of data from the sqlite database
    df = pd.read_sql('''SELECT * FROM crime_ml''', con = engine)
    sql_crime = df.to_dict('records')


    # Return template and data
    return jsonify(sql_crime)
##################################################
# create route that renders index.html template
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# create route that renders page1.html template
@app.route("/page1", methods=["GET"])
def page1():
    return render_template("page1.html")
 

if __name__ == "__main__":
    app.run(debug=True)
