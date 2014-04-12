from bottle import request, route, run, template

@route("/")
def hello():
 texte="zelkg"
 return template("html",{'variable':texte})

# mise en route du serveur
run(host="localhost", port=8000, reloader=True)
