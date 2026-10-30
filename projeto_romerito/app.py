from flask import Flask
from database import Base, engine
import models
from blueprints.index import index_bp
from blueprints.auth import auth_bp
from blueprints.ongs import ongs_bp
from blueprints.users import users_bp
from blueprints.doacoes import doacoes_bp
from blueprints.instituicoes import instituicoes_bp
from blueprints.pedidos import pedidos_bp

app = Flask(__name__)
app.secret_key = "segredo"

app.register_blueprint(index_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(ongs_bp)
app.register_blueprint(users_bp)
app.register_blueprint(doacoes_bp)
app.register_blueprint(instituicoes_bp)
app.register_blueprint(pedidos_bp)

Base.metadata.create_all(engine)

if __name__ == "__main__":
    app.run(debug=True)



