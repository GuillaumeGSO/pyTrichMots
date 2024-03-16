import flask
from flask import request, jsonify
from seek_words import search_in_file

app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/simple/<string:lang>', methods=['GET'])
def simple(lang):
    nbcar = request.args.get('nbcar')
    lstcar = list(request.args.get('lstcar'))
    return jsonify(list(search_in_file(lang, nbcar, lstcar)))
    """
    testing URL
    http://127.0.0.1:5000/simple/fr?nbcar=8&lstcar=a,b,c,e,r,t,y,u,i,i,f
    http://127.0.0.1:5000/simple/en?nbcar=5&lstcar=m,e,r,d,e
    """


app.run()