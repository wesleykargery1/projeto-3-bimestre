from sqlalchemy import String, Text, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import List, Optional
from database import Base


class Usuarios(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(80), nullable=False)
    email: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(255), nullable=False)

    doacoes: Mapped[List["Doacao"]] = relationship(
        back_populates="usuario"
    )


class Doacao(Base):
    __tablename__ = "doacoes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    valor: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), nullable=False)
    ong_id: Mapped[Optional[int]] = mapped_column(ForeignKey("ongs.id"), nullable=True)
    pedido_ajuda_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("pedidos_ajuda.id"),
        nullable=True
    )
    data_doacao: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    usuario: Mapped["Usuarios"] = relationship(
        back_populates="doacoes"
    )

    pedido_ajuda: Mapped[Optional["PedidoDeAjuda"]] = relationship(
        back_populates="doacoes"
    )

    ong: Mapped[Optional["Ong"]] = relationship(
        back_populates="doacoes"
    )


class Instituicao(Base):
    __tablename__ = "instituicoes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    cnpj: Mapped[str] = mapped_column(String(18), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(255), nullable=False)

    pedidos_ajuda: Mapped[List["PedidoDeAjuda"]] = relationship(
        back_populates="instituicao"
    )


class Ong(Base):
    __tablename__ = "ongs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str] = mapped_column(Text, nullable=False)

    projetos: Mapped[List["ProjetoSocial"]] = relationship(
        back_populates="ong"
    )

    doacoes: Mapped[List["Doacao"]] = relationship(
        back_populates="ong"
    )


class Beneficiario(Base):
    __tablename__ = "beneficiarios"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(80), nullable=False)
    pedido_ajuda_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("pedidos_ajuda.id"),
        nullable=True
    )

    pedido_ajuda: Mapped[Optional["PedidoDeAjuda"]] = relationship(
        back_populates="beneficiarios"
    )


class PedidoDeAjuda(Base):
    __tablename__ = "pedidos_ajuda"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str] = mapped_column(Text, nullable=False)
    instituicao_id: Mapped[int] = mapped_column(
        ForeignKey("instituicoes.id"),
        nullable=False
    )

    instituicao: Mapped["Instituicao"] = relationship(
        back_populates="pedidos_ajuda"
    )

    beneficiarios: Mapped[List["Beneficiario"]] = relationship(
        back_populates="pedido_ajuda"
    )

    doacoes: Mapped[List["Doacao"]] = relationship(
        back_populates="pedido_ajuda"
    )


class ProjetoSocial(Base):
    __tablename__ = "projetos_sociais"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ong_id: Mapped[int] = mapped_column(
        ForeignKey("ongs.id"),
        nullable=False
    )
    nome: Mapped[str] = mapped_column(String(150), nullable=False)

    ong: Mapped["Ong"] = relationship(
        back_populates="projetos"
    )