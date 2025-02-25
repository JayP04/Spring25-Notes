from bottle import route, run, request
import json

@route("/", method=["POST"])
def api():
    try:
        params = json.loads(request.body.read())
        lat, lon = params['lat'], params['lon']
    except:
        params = request.query.decode()
        lat, lon = params['lat'], params['lon']
    print("lat/lon: %s,%s" % (lat, lon))

run(host='localhost', port=8080)
