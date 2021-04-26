from flask import flask, render_template, abort
import json
import os
app = Flask (__name__)

with open("books.json") as archivo:
    datos=json.load(archivo)

@app.route('/')
def inicio():
    return render_template("inicio.html",libros=datos)