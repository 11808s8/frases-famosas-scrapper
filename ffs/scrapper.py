import requests
import db
# from categoria import Categoria
# from autor import Autor
# from frase import Frase
from bs4 import BeautifulSoup

numero_pagina=1
lista_posts = []
categoria = 'Amor'
categoria_banco = db.session.query(Categoria).filter(Categoria.categoria == categoria)
if(categoria_banco.count()==0):
    categoria_banco = Categoria()
    categoria_banco.categoria = categoria
    db.session.add(categoria_banco)
    db.session.commit()
    seq_categoria = db.session.execute(' select last_value from public.categoria_id_categoria_seq')
    for sc in seq_categoria:
    # print(seq_categoria)
        categoria_banco.id_categoria = sc[0]
else:
    categoria_banco = categoria_banco[0]
nome_categoria = categoria_banco.categoria.lower()
print(categoria_banco.id_categoria)
print("....")

url_base = 'https://www.pensador.com/frases_de_'+ nome_categoria +'/'
url_completo = url_base + str(numero_pagina) + '/'
teste = requests.get(url_completo)
# print(teste.status_code)
# print(teste.url)
# print(teste.url == url_completo)
# exit()
tamanho_anterior_lista = 0


while(numero_pagina == 1 or teste.url == url_completo):
    soup = BeautifulSoup(teste.text, 'html.parser')
    t = soup.find_all("div", class_="thought-card")
    tamanho_anterior_lista = len(lista_posts)
    for sibling in t:
        
        if sibling.find('p', class_='frase')!=None:
            frase = sibling.find('p', class_='frase')
            autor = sibling.find('span', class_='autor')
            lista_posts.append({
                            'frase':frase.get_text(),
                            'autor':autor.get_text().replace('\n','')
                        })
    # break
    numero_pagina += 1
    # print("Quantidade de frases nesta página: " + str(len(lista_posts)-tamanho_anterior_lista))
    print(numero_pagina)
    url_completo = url_base + str(numero_pagina) + '/'
    teste = requests.get(url_completo)

for post in lista_posts:
    frase_banco = db.session.query(Frase).filter(Frase.frase == post['frase'])
    if frase_banco.count()==0:
        autor_banco = db.session.query(Autor).filter(Autor.autor == post['autor'])
        if autor_banco.count() > 0:
            autor_banco = autor_banco[0]
            # print(autor_banco)
        else:
            autor_banco = Autor()
            autor_banco.autor = post['autor']
            db.session.add(autor_banco)
            db.session.commit()
            seq_autor = db.session.execute(' select last_value from public.autor_id_autor_seq')
            for sa in seq_autor:
            # print(seq_autor)
                autor_banco.id_autor = sa[0]
        
        frase_nova = Frase()
        frase_nova.id_categoria = categoria_banco.id_categoria
        frase_nova.id_autor = autor_banco.id_autor
        frase_nova.frase = post['frase']
        frase_nova.usado = False
        db.session.add(frase_nova)
        db.session.commit()

print(len(lista_posts))