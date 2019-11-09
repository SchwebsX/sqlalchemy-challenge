import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#Flask Setup
app = Flask(__name__)

#Flask Routes
@app.route("/")
def welcome():
    """list all available api routes"""
    return (
        f"Welcome to the Flask Portion of the Homework<br/>"
        "<br/>"
        f"Available Routes:<br/>"
        "<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>")

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a dict of date and precp"""
    # Query
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    # Convert list of tuples into normal list
    date_precip = list(np.ravel(results))

    return jsonify(date_precip)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a dict of date and precp"""
    # Query
    results = session.query(Station.station).all()

    session.close()

    # Convert list of tuples into normal list
    station_list = list(np.ravel(results))

    return jsonify(station_list)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a dict of date and precp"""
    # Query
    results  = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
    filter(Measurement.date > '2016-08-22').order_by(Measurement.date).\
    filter(Measurement.station == 'USC00519281').all()

    session.close()

    # Convert list of tuples into normal list
    temp_list = list(np.ravel(results))

    return jsonify(temp_list)


@app.route("/api/v1.0/<start>")
@app.route("api/v1.0/<start>/<end>")
def dates(start=None , end=None):
    



 if __name__ == '__main__':
    app.run(debug=True)