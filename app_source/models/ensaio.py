from sqlalchemy import (Column, Integer, PrimaryKeyConstraint)

from app_config.settings import Base


class Ensaio(Base):
    __tablename__ = 'ensaio'

    data = Column('data', primary_key=True)
    total_geral = Column(Integer, nullable=False)
    total_musicos = Column(Integer, nullable=False)
    encarregados = Column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('data', name='pk_ensaio_id'),
    )

    def __init__(self, dados):
        self.data = dados['data']
        self.total_geral = dados['total_geral']
        self.total_musicos = dados['total_musicos']
        self.encarregados = dados['encarregados']
