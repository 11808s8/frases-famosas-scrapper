import model
from sqlalchemy import Column, String  , Integer

class Categoria(model.base):     
    """
    
    Modelo da tabela Categoria
    :param id_categoria: <int>
    :param categoria: <string>

    """
    __tablename__ = 'categoria'

    id_categoria = Column(Integer, primary_key=True)
    categoria = Column(String)

    def __repr__(self):
        return "<Categoria(id='%s', nome='%s')>" % (
            self.id_categoria, self.categoria)
    
