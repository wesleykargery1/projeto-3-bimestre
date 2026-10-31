from flask import render_template, request, redirect, url_for, session as flask_sessao
from blueprints.ongs import ongs_bp
from database import Session, engine
from models import Ong


@ongs_bp.route('/cadastro_ongs', methods = ['GET', 'POST'])
def cadastro_ongs():
    usuario_id = flask_sessao.get('user_id')
    if not usuario_id:
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        
        if not nome or not descricao:
            return render_template("ongs/cadastro.html")
        
        with Session(bind = engine) as session:
            ong = Ong(
                nome = nome,
                descricao  = descricao
            )
            session.add(ong)
            session.commit()
            ong_id = ong.id
            return redirect(url_for('ongs.informacoes', ong_id = ong_id))
        
    return render_template("ongs/cadastro.html")



@ongs_bp.route('/informacoes/<int:ong_id>')
def informacoes(ong_id):
    usuario_id = flask_sessao.get('user_id')
    if not usuario_id:
        return redirect(url_for('auth.login'))
    with Session(bind = engine ) as session:
       ongs = session.get(Ong, ong_id)
       if not ongs:
           return 'ONG nao encontrada', 404
       dados = {
           'id' : ongs.id,
           'nome' : ongs.nome,
           'descricao' : ongs.descricao
       }
       
       return render_template('ongs/informacoes.html', ong = dados)
       
@ongs_bp.route('/trabalhos/<int:ong_id>')
def trabalhos(ong_id):
    usuario_id = flask_sessao.get('user_id')
    if not usuario_id:
        return redirect(url_for('auth.login'))
    with Session(bind = engine ) as session:
           ongs = session.get(Ong, ong_id)
           if ongs is None:
              return 'ONG não encontrada.', 404
           projetos = {
               'nome' : ongs.nome,
               'projetos' : [
            {
               'id' : projeto.id,
               'nome' : projeto.nome
            }
                for projeto in ongs.projetos
               ]
           }
           return render_template('ongs/trabalhos.html', ong = projetos)