from flask import render_template, request, redirect, url_for, session as flask_sessao
from blueprints.pedidos import pedidos_bp
from database import Session, engine
from models import Instituicao, PedidoDeAjuda
from sqlalchemy import select

@pedidos_bp.route('/cadastrar_pedido',methods=['GET','POST'])
def cadastrar():
    usuario_id = flask_sessao.get('user_id')
    if not usuario_id:
        return redirect(url_for('auth.login'))
    with Session() as session:

        instituicoes = session.scalars(
            select(Instituicao)
        ).all()

        if request.method == 'POST':
            titulo = request.form.get('titulo')
            descricao = request.form.get('descricao')
            instituicao_id = request.form.get('instituicao_id')

            if not titulo or not descricao or not instituicao_id:
                return render_template(
                    'pedidos/cadastro.html',
                    instituicoes=instituicoes,
                    erro='Preencha todos os campos.'
                )

            instituicao = session.get(
                Instituicao,
                int(instituicao_id)
            )

            if instituicao is None:
                return 'Instituição não encontrada', 404

            pedido = PedidoDeAjuda(
                titulo=titulo,
                descricao=descricao,
                instituicao_id=int(instituicao_id)
            )

            session.add(pedido)
            session.commit()

            return redirect(url_for('pedidos.listar'))

        return render_template(
            'pedidos/cadastro.html',
            instituicoes=instituicoes
        )

@pedidos_bp.route('/pedidos')
def listar():
    usuario_id = flask_sessao.get('user_id')
    if not usuario_id:
        return redirect(url_for('auth.login'))
    with Session(bind = engine) as session:
        pedidos = session.scalars(
            select(PedidoDeAjuda)
        ).all()

        return render_template(
            'pedidos/listar.html',
            pedidos=pedidos
        )

@pedidos_bp.route('/pedido/<int:pedido_id>')
def informacoes(pedido_id):
    usuario_id = flask_sessao.get('user_id')
    if not usuario_id:
        return redirect(url_for('auth.login'))
    with Session(bind = engine) as session:
       pedido = session.get(PedidoDeAjuda, pedido_id)

       if pedido is None:
        return 'Pedido não encontrado', 404

       return render_template(
        'pedidos/informacoes.html',
        pedido=pedido
        )