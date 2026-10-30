from flask import render_template, request, redirect, url_for, session as sf
from blueprints.instituicoes import instituicoes_bp
from database import Session
from models import Instituicao
from werkzeug.security import generate_password_hash
from sqlalchemy import select


@instituicoes_bp.route('/cadastro_instituicao', methods=['GET', 'POST'])
def cadastro():
    usuario_id = sf.get('user_id')
    if not usuario_id:
        return render_template('auth/login.html')
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        cnpj = request.form.get('cnpj')
        senha = request.form.get('senha')

        if not nome or not email or not cnpj or not senha:
            return render_template(
                'instituicoes/cadastro.html',
                erro='Prencha todos os campos.'
            )
        with Session() as session:
         instituicao = Instituicao(
            nome=nome,
            email=email,
            cnpj=cnpj,
            senha=generate_password_hash(senha)
        )

         session.add(instituicao)
         session.commit()
         return redirect(url_for('instituicoes.listar'))
    return render_template('instituicoes/cadastro.html')

@instituicoes_bp.route('/instituicoes')
def listar():
    usuario_id = sf.get('user_id')
    if not usuario_id:
        return render_template('auth/login.html')
    with Session() as session:
        instituicoes = session.scalars(
            select(Instituicao)
        ).all()

        return render_template(
            'instituicoes/listar.html',
            instituicoes=instituicoes
        )

@instituicoes_bp.route('/instituicao/<int:instituicao_id>')
def informacoes(instituicao_id):
    usuario_id = sf.get('user_id')
    if not usuario_id:
        return render_template('auth/login.html')
    with Session() as session:
        instituicao = session.get(Instituicao, instituicao_id)

        if instituicao is None:
            return 'Instituição não encontrada', 404

        return render_template(
            'instituicoes/informacoes.html',
            instituicao=instituicao
        )
