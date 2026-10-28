from models import Usuario, Instituicao, Doacao
from database import engine
from sqlalchemy.orm import Session
## NAO ESTÁ FUNCIONANDO
with Session(bind=engine) as session:
    usuario = Usuario(nome="Wesley", email="wesley.com@gmail", senha = 123)
    instituicao = Instituicao(nome="Crianca esperanca", email = "crianca.esperanca@gmail.com", senha = 12)
    doacao = Doacao(valor = 1500)

    session.add(usuario)
    session.add(instituicao)
    session.add(doacao)
    session.commit()