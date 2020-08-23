from app.model.flights import Flights
import random, string
from flask_seeder import Seeder, Faker, generator

class Flight(Flights):
    def __init__(self, flight_number=None, departure_port=None, \
            arrival_port=None, departure_time=None, arrival_time=None):
        self.flight_number = flight_number
        self.departure_port = departure_port
        self.arrival_port = arrival_port
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def __str__(self):
        return ""
