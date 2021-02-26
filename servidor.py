'''

Desenvolvedores:
    @AdrlVMA & @MayconCarvalho

-----------------------------------------------------------------------------------------
Classe Servidor - Comunicação RCP
-----------------------------------------------------------------------------------------

Fontes:

'''

import rpyc

class Servidor(rpyc.Service):

    def __init__(self):
        self.__mensagens = []
    
    def on_connect(self, conn):
        
        # Ao conectar guarde uma mensagem de entrada
        return "Você está conectado. Agora diga seu nome, bocó."

    def on_disconnect(self, conn):
        
        # Finalize guardando uma mensagem de saída
        return "Você quer sair? Então vai...!!!"

    def exposed_informe_nome(self, nome):
        info = "Entrou no chat."

        msm = {

            nome: info

        }

        self.__mensagens.append(msm)

        return "Você ({}) está no chat.".format(nome)

    def exposed_return_mensage(self, nome, last_mensage):
        return self.__mensagens[last_mensage:]


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(Servidor, port=18861)
    t.start()