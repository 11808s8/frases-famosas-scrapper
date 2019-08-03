import model
from sqlalchemy import Column, String  , Integer


class Autor(model.base):
    
    """
    
    Modelo da tabela Autor

    :param id_autor: <int>
    :param autor: <string>

    """
    __tablename__ = 'autor'

    id_autor = Column(Integer, primary_key=True)
    autor = Column(String)

    def __repr__(self):
        return "<Autor(id='%s', nome='%s')>" % (
            self.id_autor, self.autor)
    
