from . import model
from sqlalchemy import Column, String  , Integer, DateTime, Boolean
from datetime import datetime


class Frase(model.base):
    """
    
    Modelo da tabela Frase

    :param id_frase: <int>
    :param frase: <string>
    :param id_autor: <int>
    :param id_categoria: <int>
    :param date_created: <date>
    :param usado: <boolean>

    """
    __tablename__ = 'frase'

    id_frase = Column(Integer, primary_key=True)
    frase = Column(String)
    id_autor = Column(Integer)
    id_categoria = Column(Integer)
    date_created = Column(DateTime, default=datetime.now())
    usado = Column(Boolean)

    def __repr__(self):
        return "<Frase(id='%s', frase='%s', id_autor='%s', id_categoria='%s', date_created='%s', usado='%s')>" % (
            self.id_frase, self.frase, self.id_autor, self.id_categoria, self.date_created, self.usado)
    
