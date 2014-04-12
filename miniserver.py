from bottle import request, route, run

@route("/", method="GET")
def hello():
	name = request.query.get("name")
	out = "<form method='POST' action=''name='tablo'><table>"
	out += "<td><input name='case1' type='text'/></td>"
	out += "</tr>"
	out += "</table>"
	out += "<input type='submit' value='Envoyer'/></form><hr/>"
	return out

@route("/", method="POST")
def reponse():
	rep  = request.forms.get("case1")
	return """
<h1>Votre choix : %s """ % (rep,)



# mise en route du serveur
run(host="localhost", port=8000, reloader=True)
