from app.model.flights import Flights
from app import response, app, db
from flask import request

#Get all data
def index():
    try:
        flights = Flights.query.all()
        data = transform(flights)
        return response.ok(data, "OK")
    except Exception as e:
        print(e)

#Get one data
def oneFlight(id):
    try:
        flight = Flights.query.filter_by(airline_code=id).first()
        if not flight:
            return response.badRequest([],"NOT OK")
        data = singleTransform(flight)
        return response.ok(data, "OK")
    except Exception as e:
        print(e)

#Store data to database
def store():
    try:
        airline_code = request.json['airline_code']
        flight_number = request.json['flight_number']
        departure_port = request.json['departure_port']
        arrival_port = request.json['arrival_port']
        departure_time = request.json['departure_time']
        arrival_time = request.json['arrival_time']

        flight = Flights(airline_code=airline_code, \
                flight_number=flight_number, departure_port=departure_port,\
                arrival_port = arrival_port, departure_time = departure_time,\
                arrival_time = arrival_time)
        db.session.add(flight)
        db.session.commit()

        return response.ok("OK", "Successfully stored data")

    except Exception as e:
        print(e)

#update data
def update(id):
    try: 
        airline_code = request.json['airline_code']
        flight_number = request.json['flight_number']
        departure_port = request.json['departure_port']
        arrival_port = request.json['arrival_port']
        departure_time = request.json['departure_time']
        arrival_time = request.json['arrival_time']
        
        flight = Flights.query.filter_by(id=id).first()
        flight.airline_code = airline_code
        flight.flight_number = flight_number
        flight.departure_port = departure_port
        flight.arrival_port = arrival_port
        flight.departure_time = departure_time
        flight.arrival_time = arrival_time

        db.session.commit()
        return response.ok("OK", "Successfully update data")

    except Exception as e:
        print(e)
        
#delete data
def delete(id):
    try:
        flight = Flights.query.filter_by(id=id).first()
        if not flight:
            return response.badRequest("NOT OK", "Data not found")

        db.session.delete(flight)
        db.session.commit()

        return response.ok("OK", "Successfully delete data")
    except Exception as e:
        print(e)

#Transform data into Array
def transform(flights):
    array = []
    for i in flights:
        array.append(singleTransform(i))
    return array
#Transform data into python dict/object
def singleTransform(flight):
    data = {
            'id' : flight.id,
            'airline_code' : flight.airline_code,
            'flightNumber' : flight.flight_number,
            'departurePort' : flight.departure_port,
            'arrivalPort' : flight.arrival_port,
            'departureTime' : flight.departure_time,
            'arrivalTime' : flight.arrival_time,
    }

    return data
