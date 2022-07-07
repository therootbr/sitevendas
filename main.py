from flask import Flask, render_template
import json

app = Flask(__name__)

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

app.run(host='0.0.0.0', port=81)