from flask import render_template, session as sf
from blueprints.users import users_bp
from database import Session, engine
from models import Usuarios


@users_bp.route('/perfil/<int:user_id>')
def perfil(user_id):
    usuario_id = sf.get('user_id')
    if not usuario_id:
        return render_template('auth/login.html')
    with Session(bind = engine ) as session:
        usuario = session.get(Usuarios, user_id)
        if usuario:
            dados ={
            'nome' : usuario.nome,
            'email' : usuario.email
            }
        if not usuario:
            return 'Usuario nao encontrado', 404
        
    return render_template('users/perfil.html', usuario = dados )