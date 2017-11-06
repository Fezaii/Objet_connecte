from bottle import Bottle
from bottle import request
from bottle import run
import json
from sensors_actions import *
app = Bottle()



@app.get('/light')
def get_light():
    return json.dumps({'status':'ON'})

@app.post('/light')
def post_light():
    status = request.json.get("status")
    if status == 'ON':
        print("Switching the light on.")
        peluche.change_light(True)
    else:
        print("Switching the light off.")
        peluche.change_light(False)
    return #json.dumps({'status':status})

def start_REST_server(_peluche):
    """
    Start the REST server.
    You should probably spawn this in a sperate thread, as this function will
    never return.
    """
    global peluche
    peluche = _peluche
    run(app, host='0.0.0.0', port=7896, debug=True)