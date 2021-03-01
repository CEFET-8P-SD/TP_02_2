"""

Desenvolvedores:
    @AdrlVMA & @MayconCarvalho

-----------------------------------------
Classe Servidor - Comunicação RCP
-----------------------------------------

Fontes:

"""

from datetime import datetime
import rpyc
from rpyc.utils.server import ThreadedServer

mensagens = []


class Servidor(rpyc.Service):
    global mensagens

    def on_connect(self, conn):
        # Ao conectar guarde uma mensagem de entrada
        return "Você está conectado. Agora diga seu nome, bocó."

    def on_disconnect(self, conn):
        # Finalize guardando uma mensagem de saída
        return "Você quer sair? Então vai...!!!"

    def exposed_informe_nome(self, nome):
        hora = datetime.now().strftime('%H:%M:%S')

        msg = "{} {}: Entrou no chat.".format(hora, nome)

        mensagens.append(msg)

        return "Você ({}) está no chat.".format(nome)

    def exposed_enviar_mensagem(self, nome, msg):
        hora = datetime.now().strftime('%H:%M:%S')

        mensagem = "{} {}: {}".format(hora, nome, msg)

        mensagens.append(mensagem)

    def exposed_return_mensage(self, last_mensage):
        return mensagens[last_mensage:]


if __name__ == "__main__":
    t = ThreadedServer(Servidor, port=18861)
    t.start()
