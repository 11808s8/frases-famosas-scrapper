from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker

db_string = "postgres://postgres:postgres@localhost/frases_scrapper"
db = create_engine(db_string)  
Session = sessionmaker(db)  
session = Session()