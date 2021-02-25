"""

Desenvolvedores:
    @AdrlVMA & @MayconCarvalho

-----------------------------------------------------------------------------------------
Classe Servidor - Comunicação RCP
-----------------------------------------------------------------------------------------

Fontes:

"""

import rpyc
import random
from rpyc.utils.server import ThreadedServer


class Server(rpyc.Service):

    # code that runs when a connection is created
    def on_connect(self, conn):
        print('Server RPC iniciado')
        self.conexao_feita()
        print(self.exposed_fibonnaci(random.randint(5, 15)))

    # code that runs after the connection has already closed
    # (to finalize the service, if needed)
    def on_disconnect(self, conn):
        print('on_disconnect')

    # este e um metodo não exposto
    def conexao_feita(self):
        print('conexao realizada com sucesso')

    # este e um metodo exposto
    def exposed_fibonnaci(self, n: int) -> []:
        if n == 1:
            return [1]
        if n == 2:
            return [1, 1]

        values = [1, 1]
        for _ in range(2, n):
            values.append(values[-1] + values[-2])
        return values


if __name__ == '__main__':
    server = ThreadedServer(Server, port=12345)
    server.start()
