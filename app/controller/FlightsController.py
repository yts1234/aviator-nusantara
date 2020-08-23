from app.model.flights import Flights
from app import response, app


def index():
    try:
        flights = Flights.query.all()
        data = transform(flights)
        return response.ok(data, "OK")
    except Exception as e:
        print(e)

def oneFlight(id):
    try:
        flight = Flights.query.filter_by(airline_code=id).first()
        if not flight:
            return response.badRequest([],"NOT OK")
        data = singleTransform(flight)
        return response.ok(data, "OK")
    except Exception as e:
        print(e)

def transform(flights):
    array = []
    for i in flights:
        array.append(singleTransform(i))
    return array

def singleTransform(flight):
    data = {
            'airline_code' : flight.airline_code,
            'flightNumber' : flight.flight_number,
            'departurePort' : flight.departure_port,
            'arrivalPort' : flight.arrival_port,
            'departureTime' : flight.departure_time,
            'arrivalTime' : flight.arrival_time,
    }

    return data
