from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from seek_words import search_in_file, search_in_many_files
import time

app = FastAPI()
# app.config["DEBUG"] = True

@app.get("/")
def home() -> Response:
    return Response("Server is running ! !")

@app.get('/simple/{lang}')
def simple(lang:str, nbcar:str, lstcar:str) -> JSONResponse:
    #     """
    #     testing URL
    #     http://127.0.0.1:5000/simple/fr?nbcar=8&lstcar=abcertyuiif
    #     http://127.0.0.1:5000/simple/en?nbcar=5&lstcar=merde
    #     """
    start_time = time.time()
    results = list(search_in_file(lang, nbcar, lstcar))
    end_time = time.time()
    return buildResponse(results, end_time - start_time)

@app.get('/multiple/{lang}')
def multi(lang:str, lstcar:str) -> JSONResponse:
    #     """
    #     testing URL
    #     http://127.0.0.1:5000/multiple/fr?lstcar=guillaume
    #     http://127.0.0.1:5000/multiple/en?lstcar=william
    #     """
    start_time = time.time()
    results = list(search_in_many_files(lang, lstcar))
    end_time = time.time()
    return buildResponse(results, end_time - start_time)


def buildResponse(results, time):
    return JSONResponse({  
        "time": time,
        "total": len(results),
        "result": results
        })

