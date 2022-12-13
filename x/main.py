from flask import Flask, render_template, request, redirect, session, flash, url_for
from models.pessoa import Pessoa
from models.usuario import Usuario

pessoas = [
    Pessoa('Lirinha', 19, 1.71, 'Sp'),
    Pessoa('Cleitinho', 24, 1.30, 'Mg'),
    Pessoa('Jorge', 82, 1.21, 'Sc')
]

Usuario = [
    Usuario('Lirinha', 'LordLira', '2345678'),
    Usuario('Cleitinho', 'Cleitonrasta', '859600'),
    Usuario('Jorge', 'Jorginhodadoze', '556600')
]

usuario = {
    usuario    
}


app = Flask(__name__)
app.secret_key = 'senha123'


@app.route('/')
def inicio():
    return render_template('index.html', pessoas = pessoas, title = 'Home')


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login'), proximo=url_for('novo'))
    
    return render_template('novo.html')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']
    estado = request.form['estado']

    pessoas.append(Pessoa(nome, idade, altura, estado))
    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html', titulo = 'Login Usuario')


@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios :
        
        usuario = usuarios[request.form['usuario']]

        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            
            flash(usuario.nickname + ' salvo')
            proxima_pagina = request.form['proximo']
            return redirect(proxima_pagina)
        
        else:
            flash('usuario ou senha incorretos')
            return redirect('login')
        
        flash(session['usuario_logado'] + ' salvo')
        return redirect('/')
    else:
        flash('senha ou usuario incorretos')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    
    session.close()
    
    flash('voce foi quicado')
    return redirect(url_for('login'))


app.run(debug=True)