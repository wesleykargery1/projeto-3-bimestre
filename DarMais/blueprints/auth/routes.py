from flask import render_template, request, redirect, url_for, flash
from blueprints.auth import auth_bp
from models import Usuarios
from database import engine
from sqlalchemy.orm import Session

@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = Usuarios(
            nome = request.form.get('nome'),
            email = request.form.get('email'),
            senha = request.form.get('senha')
        )
        with Session(bind = engine) as session:
            session.add(usuario)
            session.commit()

@auth_bp.route('/logout')
def logout():
    return redirect(url_for("index.index"))


@auth_bp.route('/cadastro', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect(url_for("auth.register"))
    return render_template("auth/cadastro.html")
