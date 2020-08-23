from app import response, app


def index():
    return response.ok("Hai Dari Controller PT Aviator Nusantara!", "OK")
