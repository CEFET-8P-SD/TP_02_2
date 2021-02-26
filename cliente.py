'''

Desenvolvedores:
    @AdrlVMA & @MayconCarvalho

-----------------------------------------------------------------------------------------
Classe Cliente - Comunicação RCP
-----------------------------------------------------------------------------------------

Fontes:

'''

from datetime import datetime
from threading import Thread
import rpyc

last_msg = 0

def receber_mensagem():
    global last_msg

    ultimo = 0.0
    while True:
        try:
            s_atual = datetime.now().second
            if abs(s_atual-ultimo) > 0.5: 
                msg = server.root.exposed_return_mensage(last_msg)
                ultimo = s_atual

                last_msg += len(msg)

                if len(msg)>0:
                    for m in msg:
                        print(m)
        except OSError:
            break


print("Olá, seja bem vindo ao chat Educado.")

server = rpyc.connect("localhost", 18861)
nome = input("Diga seu nome:")

nome_resp = server.root.exposed_informe_nome(nome)

print(nome_resp)

receive_thread = Thread(target=receber_mensagem)
receive_thread.start()

last_msg = 0

while True:
    msg = input()
    server.root.exposed_enviar_mensagem(nome, msg)
    last_msg+=1
