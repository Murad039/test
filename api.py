#extract input from url segments
from flask import Flask

app = Flask(__name__)
@app.route('/sum/<int:x>/<int:y>')  # route to the root of our website, i.e., http://127.0.0.1
def add(x=None , y= None):
    sum = x + y
    return {"result ": sum}
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 50100,debug= True)

