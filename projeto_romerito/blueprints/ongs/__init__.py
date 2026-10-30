from flask import Blueprint

ongs_bp = Blueprint("ongs", __name__, template_folder="templates")

from blueprints.ongs import routes