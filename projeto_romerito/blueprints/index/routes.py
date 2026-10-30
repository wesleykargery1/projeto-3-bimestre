from blueprints.index import index_bp
from flask import render_template, session as sf
from sqlalchemy import select
from database import Session, engine
from models import Instituicao
@index_bp.route('/')
def index():
    usuario_id = sf.get('user_id')
    if usuario_id:
        with Session(bind = engine) as session:
          inst = session.scalars(select(Instituicao)).all()
          return render_template("index/index.html", instituicoes= inst)
    
    return render_template('auth/login.html')

