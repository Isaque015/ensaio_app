from sqlalchemy import (Column, Integer, PrimaryKeyConstraint, String)
from sqlalchemy.orm import relationship

from app_source.models import Base


class Naipe(Base):

    __tablename__ = 'naipe'

    nome = Column('nome', String, primary_key=True)
    instrumento = relationship("Instrumento")

    def __init__(self, dados):
        self.nome = dados['nome']

    __table_args__ = (
        PrimaryKeyConstraint('nome', name='pk_naipe'),
    )
