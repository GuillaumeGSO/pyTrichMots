import flask
from flask import request, jsonify
from seek_words import searchInFile

app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/simple', methods=['GET'])
def simple():
    nbcar = request.args.get('nbcar')
    lstcar = list(request.args.get('lstcar'))
    return jsonify(list(searchInFile(nbcar, lstcar)))
    """
    Pour tester
    http://127.0.0.1:5000/simple?nbcar=9&lstcar=a,b,c,e,r,t,y,u,i,i,f
    http://127.0.0.1:5000/simple?nbcar=5&lstcar=m,e,r,d,e
    """


app.run()