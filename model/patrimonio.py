from sqlalchemy import Column, String, Integer, Float
from typing import Union
from model import Base, Setor


class Patrimonio(Base):
    __tablename__ = 'patrimonio'
    id = Column("pk_patrimonio", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    quantidade = Column(Integer)
    valor = Column(Float)
    fabricante = Column(String(140))
    modelo = Column(String(140))
    setor = Column(String(140))

    # Definição do relacionamento entre o item e setor da empresa.

    def __init__(self, nome: str, quantidade: int, valor: float, fabricante: str, modelo: str, setor: str):
        """
        Cria um patrimonio

        Arguments:
            nome: nome do patrimonio.
            quantidade: quantidade que se espera comprar daquele patrimonio
            valor: valor esperado para o patrimonio
        """
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        self.fabricante = fabricante
        self.modelo = modelo
        self.setor = setor
