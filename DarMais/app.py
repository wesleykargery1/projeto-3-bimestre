from flask import Flask
from database import Base, engine
from blueprints.index import index_bp
from models import Usuarios, Instituicao, Doacao
from blueprints.auth import auth_bp

app = Flask(__name__)
app.secret_key = "segredo"

app.register_blueprint(index_bp)
app.register_blueprint(auth_bp)

Base.metadata.create_all(engine)

if __name__ == "__main__":
    app.run(debug=True)






