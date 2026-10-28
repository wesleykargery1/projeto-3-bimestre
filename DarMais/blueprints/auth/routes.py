from blueprints.auth import auth_bp
from flask import Flask, render_template, request, url_for, redirect
from models import Usuario
from database import Session, engine

@auth_bp.route('/login', methods =["GET", "POST"])
def form():
    if request.method == "POST":
        usuario = Usuario(
            nome = request.form.get('nome'),
            email = request.form.get('email'),
            senha = request.form.get('senha')
        )
        with Session(bind = engine) as session:
            session.add(usuario)
            session.commit()
        return redirect(url_for('index.index'))
    
    return redirect(url_for('alguma_coisa'))
    
    
            
        

@auth_bp.route('/logout')
def logout():
    session.pop(usuario)
    return redirect(url_for('index.index'))