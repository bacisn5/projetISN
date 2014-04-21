# -*- coding: utf-8 -*-
from bottle import request, route, run, template, get
@route("/", method="GET")
def affiche():
    return template("formulaire.html")
@route("/action1", method="GET")

def action1(): 
    concentration=float(request.query.get("cm"))
    concentration1=float(request.query.get("cf"))
    volume=float(request.query.get("vf"))
    return "Volume a prelever vaut :"+str(concentration*volume/concentration1)
#template("fonctiondilution.py ")
# elif :
#    return "Vous n'avez pas tout compléter"
# mise en route du serveur
run(host="localhost", port=8000, reloader=True)
