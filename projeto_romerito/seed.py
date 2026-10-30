from sqlalchemy import select
from werkzeug.security import generate_password_hash
from database import Session
from models import (
    Usuarios,
    Instituicao,
    Ong,
    ProjetoSocial,
    PedidoDeAjuda,
    Beneficiario,
    Doacao
)


def popular_banco():
    with Session() as session:

        # USUARIOS
        usuario1 = session.scalar(
            select(Usuarios).where(Usuarios.email == "romis@email.com")
        )
        if usuario1 is None:
            usuario1 = Usuarios(
                nome="Romerito",
                email="romis@email.com",
                senha=generate_password_hash("123456")
            )
            session.add(usuario1)

        usuario2 = session.scalar(
            select(Usuarios).where(Usuarios.email == "pedro@email.com")
        )
        if usuario2 is None:
            usuario2 = Usuarios(
                nome="Pedro Miguel",
                email="pedro@email.com",
                senha=generate_password_hash("123456")
            )
            session.add(usuario2)

        # INSTITUICOES
        instituicao1 = session.scalar(
            select(Instituicao).where(
                Instituicao.email == "crianca.esperanca@email.com"
            )
        )
        if instituicao1 is None:
            instituicao1 = Instituicao(
                nome="riança Esperança",
                email="crianca.esperanca@email.com",
                cnpj="00.000.000/0001-01",
                senha=generate_password_hash("123456")
            )
            session.add(instituicao1)

        instituicao2 = session.scalar(
            select(Instituicao).where(
                Instituicao.email == "palacio.sabedoria@email.com"
            )
        )
        if instituicao2 is None:
            instituicao2 = Instituicao(
                nome="Palácio da Sabedoria",
                email="palacio.sabedoria@email.com",
                cnpj="00.000.000/0001-02",
                senha=generate_password_hash("123456")
            )
            session.add(instituicao2)

        # ONGS
        ong1 = session.scalar(
            select(Ong).where(Ong.nome == "Mãos Solidárias")
        )
        if ong1 is None:
            ong1 = Ong(
                nome="Mãos Solidárias",
                descricao="Organização que desenvolve ações de apoio a famílias em situação de vulnerabilidade."
            )
            session.add(ong1)

        ong2 = session.scalar(
            select(Ong).where(Ong.nome == "PetsFriends")
        )
        if ong2 is None:
            ong2 = Ong(
                nome="PetsFriends",
                descricao="Organização voltada para ações de cuidado a animais de rua e em situações deploráveis."
            )
            session.add(ong2)
        session.flush()

        # PROJETOS SOCIAIS
        projeto1 = session.scalar(
            select(ProjetoSocial).where(
                ProjetoSocial.ong_id == ong1.id,
                ProjetoSocial.nome == "Alimentação para Todos"
            )
        )
        if projeto1 is None:
            session.add(
                ProjetoSocial(
                    ong=ong1,
                    nome="Alimentação para Todos"
                )
            )

        projeto2 = session.scalar(
            select(ProjetoSocial).where(
                ProjetoSocial.ong_id == ong2.id,
                ProjetoSocial.nome == "Acolhimento e Bem-Estar"
            )
        )
        if projeto2 is None:
            session.add(
                ProjetoSocial(
                    ong=ong2,
                    nome="Acolhimento e Bem-Estar"
                )
            )

        # PEDIDOS DE AJUDA
        pedido1 = session.scalar(
            select(PedidoDeAjuda).where(
                PedidoDeAjuda.titulo == "Cestas básicas para famílias"
            )
        )
        if pedido1 is None:
            pedido1 = PedidoDeAjuda(
                titulo="Cestas básicas para famílias",
                descricao="Arrecadação de alimentos para atender famílias em situação de vulnerabilidade.",
                instituicao=instituicao1
            )
            session.add(pedido1)

        pedido2 = session.scalar(
            select(PedidoDeAjuda).where(
                PedidoDeAjuda.titulo == "Materiais de higiene para idosos"
            )
        )
        if pedido2 is None:
            pedido2 = PedidoDeAjuda(
                titulo="Materiais de higiene para idosos",
                descricao="Arrecadação de materiais de higiene pessoal para os idosos atendidos pela instituição.",
                instituicao=instituicao2
            )
            session.add(pedido2)

        session.flush()

        # BENEFICIARIOS
        beneficiario1 = session.scalar(
            select(Beneficiario).where(
                Beneficiario.nome == "Maria Oliveira",
                Beneficiario.pedido_ajuda_id == pedido1.id
            )
        )
        if beneficiario1 is None:
            session.add(
                Beneficiario(
                    nome="Maria Oliveira",
                    pedido_ajuda=pedido1
                )
            )

        beneficiario2 = session.scalar(
            select(Beneficiario).where(
                Beneficiario.nome == "José Ferreira",
                Beneficiario.pedido_ajuda_id == pedido2.id
            )
        )
        if beneficiario2 is None:
            session.add(
                Beneficiario(
                    nome="José Ferreira",
                    pedido_ajuda=pedido2
                )
            )

        # DOACOES
        doacao1 = session.scalar(
            select(Doacao).where(
                Doacao.usuario_id == usuario1.id,
                Doacao.ong_id == ong1.id,
                Doacao.pedido_ajuda_id.is_(None)
            )
        )
        if doacao1 is None:
            session.add(
                Doacao(
                    valor=100.00,
                    usuario=usuario1,
                    ong=ong1
                )
            )

        doacao2 = session.scalar(
            select(Doacao).where(
                Doacao.usuario_id == usuario2.id,
                Doacao.pedido_ajuda_id == pedido2.id
            )
        )
        if doacao2 is None:
            session.add(
                Doacao(
                    valor=75.00,
                    usuario=usuario2,
                    pedido_ajuda=pedido2
                )
            )

        session.commit()
        print("Seed executado com sucesso!")


if __name__ == "__main__":
    popular_banco()
