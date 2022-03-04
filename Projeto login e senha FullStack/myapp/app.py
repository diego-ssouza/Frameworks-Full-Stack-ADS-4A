from asyncio.windows_events import NULL
from threading import local
from flask import Flask,render_template, request
from model import engine
from flask_simplelogin import SimpleLogin, Login_required
from flask_bootstrap import Bootstrap


app = Flask(__name__)

app.config ['TITTLE'] = "Arquitetura MVC"

Bootstrap(app)

@app.route("/registry", methods =["GET","POST"])
def cadastrar():
	resultado =''
	if request.method == "POST":
		name = request.form.get('UserName')
		email = request.form.get('email')
		password = request.form.get('password')
		resultado = engine.CadastrarUsuario(name,email,password)
	return render_template('registry.html', **locals())

@app.route("/login", methods =["GET","POST"])
def logar():
	resultado =''
	if request.method == "POST":
		email = request.form.get('email')
		password = request.form.get('password')
		resultado = engine.VerificarUsuario(email,password)
	return render_template('login.html', **locals())

@app.route("/users", methods =["GET"])
def Users():
	resultado = engine.TodosUsuarios()
	return render_template('listusers.html',users =resultado)