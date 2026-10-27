from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    nome: Mapped[String] = mapped_column(String(80), nullable=False)
    email: Mapped[String] = mapped_column(String(80), unique=True)
    senha: Mapped[int] = mapped_column(nullable = False)

    

class Doacao(Base):
    __tablename__ = 'doacoes'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    valor: Mapped[int] = mapped_column(nullable=False)
class Instituicao(Base):
    
    __tablename__ = "instituicoes"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    nome: Mapped[String] = mapped_column(String(100), nullable=False)
    email: Mapped[String] = mapped_column(String(80), nullable=False)
    senha: Mapped[int] = mapped_column(nullable = False)

    