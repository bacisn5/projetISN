from bottle import request, route, run, get, template

@route("/page_question.html", method="GET")
def affiche():
	return template("page_question.html")

# ce qu on fait ap que utilisateur est declencher action1
@get('/action1')
def action1():
    # on recupere la chaine 'nom' du formulaire on la stocke dans la variable mon_nom
    
    mon_nom = request.query.get('nom')
#on recupere le nombre de caracteres
    nb_mon_nom=len(mon_nom)
    mon_prenom = request.query.get('prenom')
    
    return template("sortie.tpl",{'lenom': mon_nom, 'nblettre' : str(nb_mon_nom)})
# on renvoit dans le fichier sortie.tpl (html) le contenu des variable lenom et nblettre voir le code du fichier sortie.tpl
# mise en route du serveur
run(host="localhost", port=8000, reloader=True)
