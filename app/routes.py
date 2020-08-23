from app import app
from app.controller import FlightsController

@app.route('/flights')
def flights():
    return FlightsController.index()
