from bottle import request, route, run, template, get

@route("/action1", method="GET")
def action1(): 
    concentration=request.query.get("cm")
    return "OK"
# mise en route du serveur
run(host="localhost", port=8000, reloader=True)