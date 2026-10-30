from flask import Blueprint

doacoes_bp = Blueprint("doacoes", __name__, template_folder="templates")

from blueprints.doacoes import routes