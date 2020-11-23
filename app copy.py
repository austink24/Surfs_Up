from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

""" The create_engine() function allows us to access and query our SQLite database file
Now let's reflect the database into our classes. """
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

"We'll create a variable for each of the classes so that we can reference them later"
Measurement = Base.classes.measurement
Station = Base.classes.station

"Finally, create a session link from Python to our database with the following code:"
session = Session(engine)

"ths following code reflects our database"
Base.prepare(engine, reflect=True)



app = Flask(__name__)
"First, create a function welcome() with a return statement."
""" def welcome():
    return
 """
""" Next, add the precipitation, stations, tobs, and temp routes that we'll need for this module into our return statement. 
We'll use f-strings to display them for our investors: """
@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')


