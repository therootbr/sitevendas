from flask import Flask, render_template
import json
from flask import flash, redirect
from database import db
from flask_migrate import Migrate
from models import Usuario

app = Flask(__name__)


app.config['SECRET_KEY'] = 'you-will-never-guess'

conexao = "sqlite:///meubanco.db"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produtos')
def produtos():
  arquivo = open("static/produtos.json")
  produtos = json.load(arquivo)
  return render_template('produtos.html', produtos=produtos)

@app.route('/clientes')
def clientes():
  arquivo = open("static/clientes.json")
  clientes = json.load(arquivo)
  return render_template('clientes.html', clientes=clientes)

@app.route('/teste_insert')
def teste_insert():
  u = Usuario("Alba Lopes", "emaildealba@hotmail.com", "1234")
  db.session.add(u)
  db.session.commit()
  return 'Dados insediros com sucesso'

@app.route('/teste_select')
def teste_select():
  u = Usuario.query.get(1)
  return u.nome

app.run(host='0.0.0.0', port=81)