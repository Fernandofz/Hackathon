def index():
	response.view = 'Institucion/index.html'
	return dict()

def verOrg():
	persona= db(db.Usuario.id==request.args(0)).select()

	response.view="Institucion/verOrg.html"
	busqueda = db(db.Usuario.id>0).select()
	return dict(persona=persona,busqueda=busqueda)
	return dict()