# -*- coding: utf-8 -*-
from bottle import request, route, run, template, get, static_file

@route("/", method="GET")
def affiche():
    return template("formulaire.html")

from bottle import static_file

@route('/css/<filename>')
def server_static(filename):
    return static_file(filename, root='./css')

@route('/img/<filename>')
def server_static(filename):
    return static_file(filename, root='./img')


@route("/action1", method="GET")
def action1(): 
    concentration=float(request.query.get("cm"))
    concentration1=float(request.query.get("cf"))
    volume=float(request.query.get("vf"))
    return template("sortiedilution.tpl",{'vm': str(concentration*volume/concentration1)})

@ route("/action2",method="GET")

def action2():
    concentrationmol=float(request.query.get("cmol"))
    massemol=float(request.query.get("mmol"))
    volume=float(request.query.get("vol"))
    return template("sortiemasse.tpl",{'m': str(concentrationmol*massemol*volume)})

# mise en route du serveur
run(host="localhost", port=8000, reloader=True)
