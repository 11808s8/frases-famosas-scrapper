from sqlalchemy import Column, Integer, String
from . import model


class ProfissaoAutor(model.base):

    """
    
    Modelo da tabela ProfissaoAutor

    :param id_profissao_autor: <int>
    :param profissao_autor: <string>

    """

    __tablename__ = "profissao_autor"

    id_profissao_autor = Column(Integer, primary_key=True)
    profissao_autor = Column(String)

    def __repr__(self):
        return "<Profissão Autr(id_profissao_autor='%s', profissao_autor='%s')>" % (
            self.id_profissao_autor, self.profissao_autor)
    