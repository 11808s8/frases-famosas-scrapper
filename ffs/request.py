import requests
from util import Util

class Request():

    _allowed_requests = ['head','get']
    
    def __init__(self,url_base_request=None):
        if(url_base_request!=None):
            self.url_base = '{0}'.format(url_base_request)
        else:
            self.url_base = url_base_request
        self.urls_completo = dict()

    def adiciona_url_completo(self, qual_url, caminho):
        if(self.__url_base_definido()):
            if(isinstance(caminho, str)):
                self.urls_completo[qual_url] = '{0}/{1}'.format(self.url_base,caminho)
            else:
                pass
        else:
            pass

    def adiciona_caminho(self,qual_url, caminho):
        if(isinstance(caminho, str)):
            self.urls_completo[qual_url] += caminho
    
    def set_url_base(self, url_base_request):
        if(isinstance(url_base_request, str)):
            self.url_base = url_base_request
        else:
            # @TODO: Throw error here
            pass
    
    def get_urls_completo_especifico(self, qual_url):
        return self.urls_completo[qual_url]
    
    def __url_base_definido(self):
        return (self.url_base != None)

    def one_request(self,caminho,qual_url, qual_busca='get', query_params=None):
        if(caminho!=None):
            # @TODO: Mensagem de erro
            pass
        if(qual_busca in self._allowed_requests ):
            nome_temporario = 'tempqwertyuiopasdfghjkl'
            
            self.urls_completo[nome_temporario] = '{0}{1}'.format(self.urls_completo[qual_url],caminho)
            # self.adiciona_url_completo(nome_temporario,caminho)
            req = None

            if(qual_busca == 'head'):
                req = self.head(nome_temporario)
            elif(qual_busca == 'get'):
                req = self.get(nome_temporario,query_params)
            
            self.remove_url(nome_temporario)

            return req



    def head(self, qual_url):
        if(self.__verifica_chave_urls_completos(qual_url)):
            return requests.head(self.urls_completo[qual_url])
        else:
            pass
    
    def get(self, qual_url, query_params=dict()):
        if(self.__verifica_chave_urls_completos(qual_url)):
            return requests.get(self.urls_completo[qual_url], params=query_params)
        else:
            pass

    def remove_url(self, qual_url):
        if self.__verifica_chave_urls_completos(qual_url):
            del self.urls_completo[qual_url]
        else:
            pass
        
    def __verifica_chave_urls_completos(self, chave):
        return Util.verifica_chave_dicionario(chave, self.urls_completo)