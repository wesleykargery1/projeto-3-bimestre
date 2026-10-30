from flask import render_template, request, redirect, url_for, session as flask_sessao
from blueprints.auth import auth_bp
from sqlalchemy import select
from database import Session, engine
from models import Usuarios
from werkzeug.security import generate_password_hash, check_password_hash

@auth_bp.route('/login', methods= ['GET', 'POST'])
def login():
        if request.method == 'POST':
         email = request.form.get('email')
         senha = request.form.get('senha')
         with Session(bind = engine) as session:
             usuario = session.scalar(select(Usuarios).where(Usuarios.email == email))

             if usuario and check_password_hash(usuario.senha, senha):
                flask_sessao['user_id'] = usuario.id
                return redirect(url_for('index.index'))

        return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    flask_sessao.pop('user_id', None)
    return redirect(url_for("auth.login"))

@auth_bp.route('/cadastro', methods= ['GET', 'POST'])
def cadastro():
    if request.method == "POST":
            nome = request.form.get('nome')
            email = request.form.get('email')
            senha = request.form.get('senha')
            hash_senha = generate_password_hash(senha)
            
            usuario = Usuarios(
                nome = nome,
                email = email,
                senha = hash_senha
            )
            with Session(bind = engine) as session:
                session.add(usuario)
                session.commit()
            return redirect(url_for('index.index'))
    return render_template("auth/cadastro.html")
