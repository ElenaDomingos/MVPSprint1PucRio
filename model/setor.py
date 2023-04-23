from sqlalchemy import Column, String, Integer
from datetime import datetime
from sqlalchemy.orm import relationship
from typing import Union

from model import Base


class Setor(Base):
    __tablename__ = 'setor'

    id = Column(Integer, primary_key=True)
    nome = Column(String(4000))

    # partimonio = relationship('Patrimonio')

    def __init__(self, nome: str):
        """
        Define o setor da empresa

        Arguments:
            nome: o nome do setor.

        """
        self.nome = nome
