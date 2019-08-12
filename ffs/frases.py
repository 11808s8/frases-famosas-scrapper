from bs4 import BeautifulSoup
from models.autor import Autor
from models.frase import Frase
from models.categorias_frases import CategoriasFrases
from models.categoria import Categoria
import unidecode
import db
from request import Request
import re

reqs = Request('https://www.frasesfamosas.com.br')
reqs.adiciona_url_completo('frases_autores', 'frases-de/')
reqs.adiciona_url_completo('frase_completa', 'frase/')

autores = db.session.query(Autor).order_by(Autor.id_autor.asc())

# autores bloquear:
# donald j trump
# sergio fernando moro

total_autores = len(autores)
autor_atual = 1

for autor in autores:
    # print(autor.link_alternativo_autor)
    if(autor.link_alternativo_autor!=None):
        caminho = '{0}/'.format(autor.link_alternativo_autor)
        # print(autor)
        # break
    else:

        nome_autor_unicode = autor.autor
        

        nome_autor_lowercase = nome_autor_unicode.lower()
        
        nome_autor_tratado = re.sub(r"[^a-zA-Z0-9 -çÇáàÁÀéèÉÈíìÍÌóòÓÒúùÚÙâãÂÃêẽÊẼĩĨîÎõÕÔôũŨÛûöÖōñÑüÜïÏäÄëË]+[°ºª]",'', nome_autor_lowercase)
        
        nome_autor_correto = nome_autor_tratado.replace(' ', '-')
        
        caminho = '{0}/'.format(nome_autor_correto)

    req = reqs.one_request(caminho, 'frases_autores','get')
    
    if(req.status_code==200):
        soup = BeautifulSoup(req.text, 'html.parser')
        posts = soup.find_all('div', class_='post')
        # print(req.url)
        # input()
        paginacao = soup.find('div', class_='fc-pagination')
        semPaginacao=False
        if(paginacao!=None): # PEGANDO PAGINAÇÃO
            ultima_pagina = paginacao.find('li', class_='last-page')
            if(ultima_pagina!=None):
                ultima_pagina = ultima_pagina.find('a', href=True)
                nro_ultima_pagina = int(ultima_pagina.get_text())
            # print(ultima_pagina)
            # print(nro_ultima_pagina)
            proxima_pagina = paginacao.find('li', class_='next')
            # print(proxima_pagina)
            if(proxima_pagina!=None):
                proxima_pagina = proxima_pagina.find('a', href=True)
                nro_proxima_pagina = 2
            # print("Sim")
        else:
            semPaginacao=True
            # print("Não")

        while(semPaginacao==True or nro_proxima_pagina<=nro_ultima_pagina):
            for post in posts:
                # link_frase_completa = post.find('a', class_='read-more')
                # ]
                # print(link_frase_completa)
                # if(link_frase_completa==None):
                frase = post.find('span', class_='whole-read-more')
                # else:
                #     print(link_frase_completa)
                #     input()
                    # req_frase_completa = reqs.one_request()
                link_frase_completa = frase['data-url-param-0']
                if(frase.find('span', class_='read-more-small')):
                    # print("BOOYAH!")
                    # input()
                    req_frase_completa = reqs.one_request(link_frase_completa,'frase_completa','get')
                    if(req_frase_completa.status_code==200):
                        soup_frase = BeautifulSoup(req_frase_completa.text, 'html.parser')
                        frase = soup_frase.find('blockquote', class_='current-phrase').find('span', class_='')
                        
                frase_banco = db.session.query(Frase).filter(Frase.frase==frase.get_text())
                if(frase_banco.count()==0):
                    frase_nova = Frase()
                    frase_nova.frase = frase.get_text()
                    frase_nova.id_autor = autor.id_autor
                    db.session.add(frase_nova)
                    db.session.commit()
                    frase_banco = db.session.query(Frase).filter(Frase.frase==frase.get_text()).first()
                    # frase_nova.
                    tags = post.find('div', class_='tags').find_all('a')
                    for tag in tags:
                        # print(tag.get_text())
                        categoria = db.session.query(Categoria).filter(Categoria.categoria==tag.get_text())
                        # print(categoria)
                        if(categoria.count()==0):
                            categoria_banco = Categoria()
                            categoria_banco.categoria = tag.get_text()
                            db.session.add(categoria_banco)
                            db.session.commit()
                            seq_categoria = db.session.execute(' select last_value from public.categoria_id_categoria_seq')
                            for sc in seq_categoria:
                            # print(seq_categoria)
                                categoria_banco.id_categoria = sc[0]
                                categoria_frase = db.session.query(CategoriasFrases).filter(CategoriasFrases.id_categoria==categoria_banco.id_categoria and CategoriasFrases.id_frase==frase_banco.id_frase)
                                if(categoria_frase.count()==0):
                                    categoria_frase_nova = CategoriasFrases()
                                    categoria_frase_nova.id_categoria = categoria_banco.id_categoria 
                                    categoria_frase_nova.id_frase = frase_banco.id_frase
                                    db.session.add(categoria_frase_nova)
                                    db.session.commit()
                        # print(tag['href'])
                    
                    # print(link_frase_completa)
                    # print(frase.get_text())
                    # print(' - {0}'.format(autor.autor))
                    # input()
            if(semPaginacao==True):
                print("Autor {0} sem paginação".format(autor.autor))
                break
            else:
                caminho_prox_pagina = "{0}?page={1}".format(caminho,nro_proxima_pagina)
                req = reqs.one_request(caminho_prox_pagina, 'frases_autores','get')
                soup = BeautifulSoup(req.text, 'html.parser')
                posts = soup.find_all('div', class_='post')
                print("Autor {0} pagina atual {1} ultima pagina {2}".format(autor.autor, nro_proxima_pagina, nro_ultima_pagina))
                nro_proxima_pagina+=1
                # print(nro_proxima_pagina)
                # print(nro_ultima_pagina)
                
                
        print("Autor nro {0}/{1}".format(autor_atual,total_autores))
                
        

        # array_link_alternativo_autor = autor_link['href'].split('/')
        # link_alternativo_autor = array_link_alternativo_autor[-2]
    # class = whole-read-more
    # print(req)

    