from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker

db_string = "postgres://postgres:postgres@localhost/frases_scrapper"
db = create_engine(db_string)  
Session = sessionmaker(db)  
session = Session()


# @TODO: Colocar um throw error aqui
def last_sequence_number(table,schema='public'):
    sequence_name = schema + '.' + table + '_id_' + table + 'seq'
    select_sequence = 'select last_value from ' + sequence_name
    seq = session.execute(select_sequence)
    for retorno in seq:
        return retorno[0]
    return None