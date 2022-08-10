# Set up the Flask Weather App
# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Set up database engine for Flask app
# Create function allows access to SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")
# Reflect database into classes
Base = automap_base()
# Reflect tables
Base.prepare(engine, reflect=True)
# Set class variables
Measurement = Base.classes.measurement
Station = Base.classes.station
# Creates session link from Python to SQLite database
session = Session(engine)
# Create Flask app, all routes go after this code
app = Flask(__name__)

@app.route("/")

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


# 9.5.3 Precipitation Route
@app.route("/api/v1.0/precipitation")

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

#9.5.4 Stations Route
@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)


