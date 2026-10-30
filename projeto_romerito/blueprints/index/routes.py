from blueprints.index import index_bp
from flask import render_template, session
from database import Session, engine
from models import Usuarios

INSTITUICOES = [
    {"nome": "Associação Apoio à Infância",
     "descricao": "Apoio escolar e alimentação para crianças em situação de vulnerabilidade."},
    {"nome": "Proteção Animal Viva",
     "descricao": "Resgate, vacinação e abrigo para animais abandonados."},
    {"nome": "Refúgio dos Idosos",
     "descricao": "Cuidados de saúde, lar e atividades de integração para idosos."},
    {"nome": "Fundo Ambiental Verde",
     "descricao": "Reflorestamento de áreas degradadas e preservação da fauna local."},
]


@index_bp.route('/')
def index():
    usuario_id = session.get('user_id')
    if usuario_id:
        return render_template("index/index.html", instituicoes=INSTITUICOES)
    
    return render_template('auth/login.html')

