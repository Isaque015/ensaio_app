from sqlalchemy import (Column, Integer, PrimaryKeyConstraint, String)

from app_config.settings import Base


class Naipe(Base):

    __tablename__ = 'naipe'

    nome = Column('nome', String, primary_key=True)
    total = Column(Integer, nullable=False)

    def __init__(self, dados):
        self.nome = dados['nome']
        self.total = dados['total']

    __table_args__ = (
        PrimaryKeyConstraint('nome', name='pk_naipe_id'),
    )
