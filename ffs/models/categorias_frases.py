from sqlalchemy import Column, Integer, String
from . import model


class CategoriasFrases(model.base):

    """
    
    Modelo da tabela CategoriasFrases

    :param id_categoria: <int>
    :param id_frase: <int>

    """

    __tablename__ = "categorias_frases"

    id_categoria = Column(Integer, primary_key=True)
    id_frase = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<Categorias Frases(id_categoria='%s', id_frase='%s')>" % (
            self.id_categoria, self.id_frase)
    