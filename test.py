import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/rate', methods=['GET'])
def rate():
    to = request.args.get('to')
    if to == None:
        return "{'error':'no to'}"

    try:
        r = requests.get("https://hatasaki.azure-api.net/fx/?from=USD&to="+to)
    except:
        return "{'error':'backedn error'}"

    content = json.loads(r.content)
    return "{'rate':'"+content["rate"]+"'}"

if __name__ == '__main__':
    app.run(port=8080, debug=True);