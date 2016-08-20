def index():
	if session.usuario!=None:
		response.view="Persona/index.html"
		persona= db(db.Usuario.Usuario==session.usuario).select()
		busqueda = db(db.Usuario.id>0).select()
		
		return dict(persona=persona,busqueda=busqueda)
	else:
		redirect(URL('home','main'))

def show():
	persona= db(db.Usuario.id==request.args(0)).select()

	response.view="Persona/index.html"
	busqueda = db(db.Usuario.id>0).select()
	return dict(persona=persona,busqueda=busqueda)

def download():
	return response.download(request,db)
