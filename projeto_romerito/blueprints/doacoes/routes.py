from flask import render_template, request, redirect, url_for, session as flask_sessao
from sqlalchemy import select
from blueprints.doacoes import doacoes_bp
from database import Session, engine
from models import Doacao, Ong, PedidoDeAjuda

@doacoes_bp.route('/doar', methods= ['GET', 'POST'])
def doar():
    usuario_id = flask_sessao.get('user_id')
    if not usuario_id:
        return redirect(url_for('auth.login'))
    with Session(bind = engine) as session:
       ongs = session.scalars(select(Ong)).all()
       pedidos = session.scalars(select(PedidoDeAjuda)).all()
       if request.method == "POST":
          valor = request.form.get('valor')
          ong = request.form.get('ong_id') or None
          pedido = request.form.get('pedido_ajuda_id') or None
          doacao = Doacao(
              valor = valor,
              usuario_id = usuario_id,
              ong_id = ong,
              pedido_ajuda_id = pedido            
              )
          session.add(doacao)
          session.commit()
          return redirect(url_for('doacoes.visualizar', doacoes_id = doacao.id))
        
    return render_template('doacoes/cadastro.html',ongs=ongs, pedidos=pedidos )


@doacoes_bp.route('/visualizar_doacoes/')
def visualizar():
     usuario_id = flask_sessao.get('user_id')
     with Session(bind = engine ) as session:
        doacoes = session.scalars(select(Doacao).where(Doacao.usuario_id == usuario_id)).all()
        return render_template('doacoes/visualizar.html', doacoes = doacoes)