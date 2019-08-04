import requests
import sys
from bs4 import BeautifulSoup
import '../db'


indice_profissao = 0
profissoes = sys.argv
qual_profissao = profissoes[indice_profissao]
url_base = 'https://www.frasesfamosas.com.br/indice/profissoes/' 
url_completo = url_base + str(qual_profissao) +'/'
req = requests.get(url_completo)
# print(req.status_code)

# executará com todas as profissões passadas pela linha de comando
while(indice_profissao<len(profissoes)):
    
    # Se o retorno for alcançável, processa
    if(req.status_code==200):
        soup = BeautifulSoup(req.text, 'html.parser')
        a_list = soup.find_all("a", rel='twipsy')
        for a in a_list:
            autor = a.get_text()
    
    indice_profissao += 1