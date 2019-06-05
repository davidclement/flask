from app import app
from flask import request, jsonify
import logging
from pprint import pprint

logging.basicConfig(filename="hw.log", level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s: %(message)s')

@app.route('/', methods=['GET','POST'])
def index():
    #pprint(dir(request))
    #pprint(request.url)
    logging.debug(request.url)
    acceptHeader = request.headers.get('Accept',None)
    if acceptHeader and acceptHeader == "application/json":
        return jsonify({"message": "Good morning"})
    else:
        return "<p>Hello, World</p>\n"


