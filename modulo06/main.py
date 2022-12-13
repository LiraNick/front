from flask import Flask, render_template, redirect, request
from funcionario import Funcionario

#
lista = [
    funcionario1 = Funcionario('nicolas', '19', '1.70')
    funcionario2 = Funcionario('cleiton', '24', '1.57')
    funcionario3 = Funcionario('jorginho', '16', '1.66')
]


app = Flask(__name__)

#
@app.route('/')
def inicio():
    return render_template('index.html', titulo = 'Lista Funcionarios', pessoas = lista)


@app.route('/new')
def new():
    return render_template('new.html', titulo = 'cadastro funcionario')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    vr = Funcionario(nome, idade, altura)

    lista.append(vr)

    return redirect('/')

app.run(debug=True) 