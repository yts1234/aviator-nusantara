# PT Aviator Nusantara API

This is API for external 3rd Party client who want to get access into Company data about flights schedule.

## Requirements
- Pyhton 3
- Pip3
- Virtual environment (python3-venv)
- Flask
- Flask-sqlalchemy
- Flask-migrate
- Pymysql
- Python-dotenv
- MySQL
- Postman

## Installing
1. Clone this repository
2. run source venv/bin/activate to activate python virtual environment. Using this you will isolate your project environment.
3. Change the DB credential in .flaskenv file
4. run flask db migrate for creating the migration file
5. run flask db upgrade for creating the database schema
6. run flask run -h 0.0.0.0 -p 8080 this will run flask localy in your server listening on your machine IP address and port 8080
7. Use Postman for testing this APIs

## API Endpoints
Below are the list of CRUD APIs

### Get All Data
GET method
```
/flights
```
### Get Subset of Data
GET method
```
/flight/[airline_code]
```
### Insert Data
POST method
```
/storeFlight
```
### Update Data
PUT method
```
/updateFlight/[id]
```
### Delete Data
DELETE method
```
/deleteFlight/[id]
```

## Example
#### Get data
http://[ip]/flights

#### Get Subset of Data
http://[ip]/flight/[airline_code]

#### Insert Data
http://[ip]/storeFlight

json body
```json
{
    "airline_code": "CA",
    "flight_number": "CA400",
    "departure_port": "US",
    "arrival_port": "UK",
    "departure_time": "2020-08-14 00:00:01",
    "arrival_time": "2020-08-15 00:02:01"
}
```
#### Update Data
http://[ip]/updateFlight/[id]

json body
```json
{
    "airline_code": "CA",
    "flight_number": "CA401",
    "departure_port": "US",
    "arrival_port": "UK",
    "departure_time": "2020-08-14 00:00:01",
    "arrival_time": "2020-08-15 00:02:01"
}
```
#### Delete Data
http://ip/deleteFlight/[id]

### Note
1. You must first populate the data yourself using the /storeFlight endpoint.
2. the [id] mean the primary key id. To get this id for delete and update process you can use the /flights endpoint to see the flight id
