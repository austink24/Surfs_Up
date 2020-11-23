from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func



engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
"ths following code reflects our database"
Base.prepare(engine, reflect=True)

"We'll create a variable for each of the classes so that we can reference them later"
Measurement = Base.classes.measurement
Station = Base.classes.station

"Finally, create a session link from Python to our database with the following code:"
session = Session(engine)


app = Flask(__name__)

@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API! <br>
    Available Routes: <br>
    /api/v1.0/precipitation <br>
    /api/v1.0/stations <br>
    /api/v1.0/tobs <br>
    /api/v1.0/temp/start/end 
    ''')

""" 
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
   return """


""" Finally, we'll create a dictionary with the date as the key and the precipitation as the value. To do this, we will "jsonify" our dictionary. 
Jsonify() is a function that converts the dictionary to a JSON file. """

@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

""" We want to start by unraveling our results into a one-dimensional array. 
To do this, we want to use thefunction np.ravel(), with results as our parameter.
Next, we will convert our unraveled results into a list. To convert the results to a list, 
we will need to use the list function, which is list(), and then convert that array 
into a list. Then we'll jsonify the list and return it as JSON. Let's add that functionality 
to our code: """

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

""" In the following code, take note of the asterisk in the query next to the set list. 
Here the asterisk is used to indicate there will be multiple results 
for our query: minimum, average, and maximum temperatures. """

if __name__=="__main__":
    app.run(host="localhost", port=8000, debug=True)