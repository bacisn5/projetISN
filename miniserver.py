from bottle import request, route, run

@route("/", method="GET")
def hello():
	name = request.query.get("name")
# on génère la page html ici
	out = "<form method='POST' action=''name='tablo'><table>"
	for i in range(1,10):
		out += "<tr>"
		for j in range(1,10):
			out += "<td><input name='row"+str(i)+'-'+str(j)+"' type='text'/></td>"
		out += "</tr>"
	out += "</table>"
	out += "<input type='submit' value='Envoyer'/></form><hr/>"
# on retourne la page html
	return out

@route("/", method="POST")


def reponse():
	rep  = request.forms.get("row11")
	return """
<h1>Votre choix : %s """ % (rep,)

# Toto
run(host="localhost", port=8123, reloader=True)
