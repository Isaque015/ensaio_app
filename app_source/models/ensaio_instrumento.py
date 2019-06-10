from sqlalchemy import (Column, PrimaryKeyConstraint, String, DateTime,
                        ForeignKeyConstraint, Integer)

from app_source.models import Base


class EnsaioInstrumento(Base):

    __tablename__ = 'ensaio_instrumento'

    nome_instrumento = Column(String)
    data_ensaio = Column(DateTime)
    total_instrumento = Column(Integer)

    __table_args__ = (
        ForeignKeyConstraint(
            ['nome_instrumento'], ['instrumento.nome'],
            name='fk_ensaioinstrumento_instrumento'
        ),
        ForeignKeyConstraint(
            ['data_ensaio'], ['ensaio.data'],
            name='fk_ensaioinstrumento_ensaio'
        ),
        PrimaryKeyConstraint(
            'nome_instrumento', 'data_ensaio', name='pk_ensaioinstrumento'
        ),
    )

    def __init__(self, dados):
        self.nome_instrumento = dados['nome_instrumento']
        self.data_ensaio = dados['data_ensaio']
        self.total_instrumento = dados['total_instrumento']
