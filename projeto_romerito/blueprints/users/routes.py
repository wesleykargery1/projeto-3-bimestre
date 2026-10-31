from flask import render_template, request, redirect, url_for, session as flask_sessao
from blueprints.users import users_bp
from database import Session, engine
from models import Usuarios


@users_bp.route('/perfil/<int:user_id>')
def perfil(user_id):
    usuario_id = flask_sessao.get('user_id')
    if not usuario_id:
        return redirect(url_for('auth.login'))
    with Session(bind = engine ) as session:
        usuario = session.get(Usuarios, user_id)
        dados ={
            'nome' : usuario.nome,
            'email' : usuario.email
            }
        if not usuario:
            return 'Usuario nao encontrado', 404
        
        return render_template('users/perfil.html', usuario = dados )