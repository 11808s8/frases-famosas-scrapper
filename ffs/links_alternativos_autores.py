from bs4 import BeautifulSoup
from models.autor import Autor
import unidecode
import db
import requests
from request import Request
import re

reqs = Request('https://www.frasesfamosas.com.br')
reqs.adiciona_url_completo('frases_autores', 'frases-de/')
reqs.adiciona_url_completo('buscar_frases', 'buscar-frases/')

autores = db.session.query(Autor)
ultimo_autor_com_link_alternativo = db.session.query(Autor).filter(Autor.link_alternativo_autor!='' or Autor.link_alternativo_autor!=None).order_by(Autor.id_autor.desc()).first()

for autor in autores:
    if(ultimo_autor_com_link_alternativo== None or autor.id_autor>ultimo_autor_com_link_alternativo.id_autor):

        nome_autor_unicode = autor.autor
        

        nome_autor_lowercase = nome_autor_unicode.lower()
        
        nome_autor_tratado = re.sub(r"[^a-zA-Z0-9 -çÇáàÁÀéèÉÈíìÍÌóòÓÒúùÚÙâãÂÃêẽÊẼĩĨîÎõÕÔôũŨÛûöÖōñÑüÜïÏäÄëË]+[°ºª]",'', nome_autor_lowercase)
        
        nome_autor_correto = nome_autor_tratado.replace(' ', '-')
        
        caminho = '{0}/'.format(nome_autor_correto)
        req = reqs.one_request(caminho, 'frases_autores','head')
        
        if(req.status_code!=200):
            print(nome_autor_lowercase)
            
            if(nome_autor_tratado.find(',')>0):
                print('a')
                nome_autor_tratado = nome_autor_tratado.replace(',', '')
            
            nome_autor_para_busca = nome_autor_tratado.replace(' ', '+')
            print(nome_autor_para_busca)
            
            req_busca = reqs.get('buscar_frases',{'q': nome_autor_para_busca})
            print(req_busca.url)
            
            if(req_busca.status_code==200):
                soup = BeautifulSoup(req_busca.text, 'html.parser')
                autor_link = soup.find('span', class_='quote-footer').find('a', href=True)
                
                array_link_alternativo_autor = autor_link['href'].split('/')
                link_alternativo_autor = array_link_alternativo_autor[-2]
                print(link_alternativo_autor)
                autor.link_alternativo_autor = link_alternativo_autor
                db.session.commit()

    else:
        pass
