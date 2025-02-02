# import json
# import time
from fastapi import FastAPI, Response
# from seek_words import search_in_file, search_in_many_files

app = FastAPI()
# app.config["DEBUG"] = True

@app.get("/")
def home() -> Response:
    return Response("Server is running ! !")

# @app.get('/simple/{lang}')
# def simple(lang):
#     nbcar = request.args.get('nbcar')
#     lstcar = list(request.args.get('lstcar'))
#     results = list(search_in_file(lang, nbcar, lstcar))
#     response = jsonify(results)
#     response.charset = "utf-8"
#     response.data = json.dumps(results, ensure_ascii=False).encode('utf8')
#     return response
#     """
#     testing URL
#     http://127.0.0.1:5000/simple/fr?nbcar=8&lstcar=abcertyuiif
#     http://127.0.0.1:5000/simple/en?nbcar=5&lstcar=merde
#     """
# @app.route('/multiple/{lang}>')
# def multi(lang):
#     cars = request.args.get('lstcar')
#     start_time = time.time()
#     results = list(search_in_many_files(lang, cars))
#     end_time = time.time()
    
#     response = jsonify(results)
#     response.charset = "utf-8"
#     response.data = json.dumps({"total": len(results), "time": end_time - start_time, "results": results}, ensure_ascii=False).encode('utf8')
#     return response
    # http://127.0.0.1:5000/multiple/fr?lstcar=guillaume
    # http://127.0.0.1:5000/multiple/en?lstcar=william


# def buildResponse(response, time):
    # return json.dump({  
    #     "total": len(response.data),
    #     "result": response.data,
    #     "time": time
    #     })

