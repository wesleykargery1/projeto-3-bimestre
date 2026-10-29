# app.py — Oficina de Conserto (versão inicial)
from flask import Flask
from database import Base, engine
from blueprints.index import index_bp
from models import Usuario, Instituicao, Doacao

app = Flask(__name__)
app.secret_key = "segredo"
app.register_blueprint(index_bp)
Base.metadata.create_all(engine)


