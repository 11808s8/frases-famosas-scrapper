import requests
import sys

from models.profissao_autor import ProfissaoAutor
from models.profissoes_autores import ProfissoesAutores
from models.autor import Autor

from bs4 import BeautifulSoup
import db


indice_profissao = 1
profissoes = sys.argv
print(profissoes)
qual_profissao = profissoes[indice_profissao]
url_base = 'https://www.frasesfamosas.com.br/indice/profissoes/' 
url_completo = url_base + str(qual_profissao) +'/'
print(url_completo)
req = requests.get(url_completo)
# print(req.status_code)

# executará com todas as profissões passadas pela linha de comando
while(indice_profissao<=(len(profissoes)-1)):
    
    # Se o retorno for alcançável, processa
    if(req.status_code==200):
        soup = BeautifulSoup(req.text, 'html.parser')
        profissao = soup.find('h1', class_='hand').find('span', class_='heading-2').get_text()
        profissao_banco = db.session.query(ProfissaoAutor).filter(ProfissaoAutor.profissao_autor == profissao)
        
        if(profissao_banco.count() == 0):
            nova_profissao = ProfissaoAutor()
            nova_profissao.profissao_autor = profissao
            
            db.session.add(nova_profissao)
            db.session.commit()

            
            nova_profissao.id_profissao_autor = db.last_sequence_number('profissao_autor')

            profissao_banco = nova_profissao
        else:
            profissao_banco = profissao_banco[0]

        # print(profissao)
        # print('a')
        a_list = soup.find_all("a", rel='twipsy')
        for a in a_list:
            autor = a.get_text()
            autor_banco = db.session.query(Autor).filter(Autor.autor == autor)
            if(autor_banco.count() == 0):
                novo_autor = Autor()
                novo_autor.autor = autor
                db.session.add(novo_autor)
                db.session.commit() 
                novo_autor.id_autor = db.last_sequence_number('autor')
                autor_banco = novo_autor
            else:
                autor_banco = autor_banco[0]
            
            profissoes_autores_banco = db.session.query(ProfissoesAutores).filter(ProfissoesAutores.id_autor == autor_banco.id_autor and ProfissoesAutores.id_profissao_autor == profissao_banco.id_profissao_autor)
            if(profissoes_autores_banco.count()==0):
                novo_profissoes_autores_banco = ProfissoesAutores()
                novo_profissoes_autores_banco.id_profissao_autor = profissao_banco.id_profissao_autor
                novo_profissoes_autores_banco.id_autor = autor_banco.id_autor
                db.session.add(novo_profissoes_autores_banco)
                db.session.commit()
    
    indice_profissao += 1