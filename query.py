from flask import Flask, request

app = Flask(__name__)

@app.route('/map', methods=['GET'])
def add():
    x = request.args.get('a', type = int)
    y = request.args.get('b', type = int)
    sum = x + y
    return {'result' : sum}

if __name__ == ('__main__'):
    app.run(host='0.0.0.0', port=5000 ,debug=True ), 200
    
