from sqlalchemy import (Column, Integer, PrimaryKeyConstraint, DateTime)
from sqlalchemy.orm import relationship

from app_source.models import Base


class Ensaio(Base):

    __tablename__ = 'ensaio'

    data = Column('data', DateTime)
    encarregados = Column(Integer, nullable=False)
    organistas = Column(Integer, nullable=False)
    irmandade = Column(Integer, nullable=False)

    ensaio_instrumento = relationship("EnsaioInstrumento")

    __table_args__ = (
        PrimaryKeyConstraint('data', name='pk_ensaio'),
    )

    def __init__(self, dados):
        self.data = dados['data']
        self.organistas = dados['organistas']
        self.irmandade = dados['irmandade']
        self.encarregados = dados['encarregados']
