from sqlalchemy import (Column, PrimaryKeyConstraint, String,
                        ForeignKeyConstraint)
from sqlalchemy.orm import relationship

from app_source.models import Base


class Instrumento(Base):

    __tablename__ = 'instrumento'

    nome = Column('nome', String)
    nome_naipe = Column(String)

    ensaio_instrumento = relationship("EnsaioInstrumento")

    def __init__(self, dados):
        self.nome = dados['nome']
        self.nome_naipe = dados['nome_naipe']

    __table_args__ = (
        PrimaryKeyConstraint('nome', name='pk_instrumento'),
        ForeignKeyConstraint(
            ['nome_naipe'], ['naipe.nome'], name='fk_instrumento_naipe'
        )
    )
