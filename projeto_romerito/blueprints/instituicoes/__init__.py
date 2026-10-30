from flask import blueprint

instituicoes_bp = Blueprint(
    "instituicoes", 
    __name__, 
    template_folder = "templates"
)

from blueprints.instituicoes import routes