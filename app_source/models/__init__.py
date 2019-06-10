from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from app_source.models.ensaio import Ensaio
from app_source.models.naipe import Naipe
from app_source.models.instrumento import Instrumento
from app_source.models.ensaio_instrumento import EnsaioInstrumento
