from sqlalchemy import Column, Integer, String
from . import model


class ProfissoesAutores(model.base):

    """
    
    Modelo da tabela ProfissaoAutor

    :param id_profissao_autor: <int>
    :param id_autor: <int>

    """

    __tablename__ = "profissoes_autores"

    id_profissao_autor = Column(Integer, primary_key=True)
    id_autor = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<Profissão Autr(id_profissao_autor='%s', profissao_autor='%s')>" % (
            self.id_profissao_autor, self.profissao_autor)
    