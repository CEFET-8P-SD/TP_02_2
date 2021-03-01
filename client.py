"""

Desenvolvedores:
    @AdrlVMA & @MayconCarvalho

-----------------------------------------------------------------------------------------
Classe Cliente - Comunicação RCP
-----------------------------------------------------------------------------------------

Fontes:

"""

from datetime import datetime
from threading import Thread
import rpyc
import tkinter
import sys

last_msg = 0
IP = str(sys.argv[1])
nome = str(sys.argv[2])


def receber_mensagem():
    global last_msg
    global nome
    msg = "Olá, seja bem vindo ao chat Educado."
    msg_list.insert(tkinter.END, msg)

    nome_resp = server.root.exposed_informe_nome(nome)

    msg_list.insert(tkinter.END, nome_resp)

    ultimo = 0.0
    while True:
        try:
            s_atual = datetime.now().second
            if abs(s_atual - ultimo) > 0.5:

                msg = server.root.exposed_return_mensage(last_msg)
                ultimo = s_atual

                last_msg += len(msg)

                if len(msg) > 0:
                    for m in msg:
                        msg_list.insert(tkinter.END, m)
        except OSError:
            break


def enviar_mensagem(event=None):
    global last_msg
    msg = my_msg.get()
    my_msg.set('')
    if msg != '{quit}' and msg != '':
        server.root.exposed_enviar_mensagem(nome, msg)
        last_msg += 1
    else:
        server.close()
        top.quit()


def fechar_chat(event=None):
    my_msg.set('{quit}')
    enviar_mensagem()


top = tkinter.Tk()
top.title('Chat usando RPC')
top.resizable(width=True, height=True)

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
my_msg.set('')

scrollbar = tkinter.Scrollbar(messages_frame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

msg_list = tkinter.Listbox(messages_frame, height=25, width=75, yscrollcommand=scrollbar.set)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg, width=65)
entry_field.bind('<Return>', enviar_mensagem)
entry_field.pack()
entry_field.focus()

send_button = tkinter.Button(top, text='Enviar', font='Helvetica 10 bold', width=20, command=enviar_mensagem)
send_button.pack()

top.protocol('WM_DELETE_WINDOW', fechar_chat)

server = rpyc.connect("localhost", 18861)

receive_thread = Thread(target=receber_mensagem)
receive_thread.start()
tkinter.mainloop()
