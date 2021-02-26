'''

Desenvolvedores:
    @AdrlVMA & @MayconCarvalho

-----------------------------------------------------------------------------------------
Classe Cliente - Comunicação RCP
-----------------------------------------------------------------------------------------

Fontes:

'''

from threading import Thread
import rpyc

class Cliente():

    def _run(self):
        print("Olá, seja bem vindo ao chat Educado.")
        
        server = rpyc.connect("localhost", 18861)
        nome = input()

        print(server.root.exposed_informe_nome(nome))

cl = Cliente()

cl._run()
