def index():
	response.view="home/Main.html"
	return dict(msj="")

def login1():
	response.view="home/LogIn.html"
	return dict(msj="")

def login():
	datos=request.post_vars
	usuario=db(db.Usuario.Usuario == datos.Usuario, db.Usuario.Pass == datos.Pass).select()
	if len(usuario)!=0:
		session.usuario = datos.Usuario
		session.tipo = usuario[0].Tipo
		redirect(URL('home','main'))
		return dict(msj="Bienvenido")

	else:
		response.view="inicio/LogIn.html"
		return dict(msj="Usuario o Contraseña invalida")

def registrar():
	response.view="home/Registrar.html"
	return dict()

def registroCorrecto():
	datos=request.post_vars
	db.Usuario.insert(Tipo=datos.tipoU,Usuario=datos.Usuario,Pass=datos.Pass,image=datos.Pic,Edad=datos.Edad,Estudios=datos.Estudio,idioma=datos.Idioma,Nombre=datos.Nombre)
	response.view="inicio/LogIn.html"
	redirect(URL('home','login1'))
	return dict(msj="")

def cerrar():
	session.usuario = None
	response.view="inicio/LogIn.html"
	redirect("index")
	return dict()

def main():
	response.view="home/Main.html"
	return dict()