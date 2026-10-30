from blueprints.index import index_bp
from flask import render_template, session as sf
from sqlalchemy import select
from database import Session, engine
from models import Instituicao,Ong
@index_bp.route('/')
def index():
    usuario_id = sf.get('user_id')
    if usuario_id:
        with Session(bind = engine) as session:
          inst = session.scalars(select(Instituicao)).all()
          ong = session.scalars(select(Ong)).all()
          return render_template("index/index.html", instituicoes= inst, ongs = ong)
    
    return render_template('auth/login.html')

