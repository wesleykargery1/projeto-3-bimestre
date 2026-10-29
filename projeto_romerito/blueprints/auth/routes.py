from flask import render_template, request, redirect, url_for, flash
from blueprints.auth import auth_bp


@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("auth.login"))
    return render_template("auth/login.html")


@auth_bp.route('/logout')
def logout():
    return redirect(url_for("index.index"))


@auth_bp.route('/cadastro', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect(url_for("auth.register"))
    return render_template("auth/cadastro.html")
