from app import app
from app.controller import FlightsController

@app.route('/flights')
def flights():
    return FlightsController.index()

@app.route('/flight/<id>')
def oneFlight(id):
    return FlightsController.oneFlight(id)

@app.route('/storeFlight', methods=['POST'])
def storeFlight():
    return FlightsController.store()

@app.route('/updateFlight/<id>', methods=['PUT'])
def updateFlight(id):
    return FlightsController.update(id)
