from app.model.flights import Flights
from app import response, app


def index():
    try:
        flights = Flights.query.all()
        data = transform(flights)
        return response.ok(data, "OK")
    except Exception as e:
        print(e)

def transform(flights):
    array = []
    for i in flights:
        array.append({
            'airline_code' : i.id,
            'flightNumber' : i.flight_number,
            'departurePort' : i.departure_port,
            'arrivalPort' : i.arrival_port,
            'departureTime' : i.departure_time,
            'arrivalTime' : i.arrival_time,
            })
    return array

