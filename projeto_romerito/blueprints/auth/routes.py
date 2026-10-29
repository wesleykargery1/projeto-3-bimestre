from flask import render_template, request, redirect, url_for, session
from blueprints.auth import auth_bp
from sqlalchemy import select
from database import Session, engine
from models import Usuarios
@auth_bp.route('/login')
def login():
        email = request.form.get('email')
        senha = request.form.get('senha')
        usuario = session.scalar(select(Usuarios).where(Usuarios.email == email))

        if usuario and usuario.senha == senha:
            session['user_id'] = usuario.id
            return redirect(url_for('index.index'))

        return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for("index.index"))

@auth_bp.route('/cadastro')
def cadastro():
    if request.method == "POST":
            usuario = Usuarios(
                nome = request.form.get('nome'),
                email = request.form.get('email'),
                senha = request.form.get('senha')
            )
            with Session(bind = engine) as session:
                session.add(usuario)
                session.commit()
            return redirect(url_for('index.index'))
    return render_template("auth/cadastro.html")