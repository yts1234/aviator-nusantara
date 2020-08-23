from app import app

@app.route('/')
def index():
    return "Hello from PT Aviator Nusantara!"
