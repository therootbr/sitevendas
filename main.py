from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produtos')
def produtos():
  arquivo = open("static/produtos.json")
  produto = json.load(arquivo)
  return render_template('produtos.html', produto=produto)

app.run(host='0.0.0.0', port=81)