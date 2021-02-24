'''

Desenvolvedores:
    @AdrlVMA & @MayconCarvalho

-----------------------------------------------------------------------------------------
Classe Cliente - Comunicação RCP
-----------------------------------------------------------------------------------------

Fontes:

'''

class Cliente():
    
    def __init__(self):
    


    #-----------------------------------------------------------------------------------------
    # Método de inicialização da interface
    #-----------------------------------------------------------------------------------------
    def __run_interface(self):

        top = tkinter.Tk()
        top.title('Protocolo UDP')
        top.resizable(width=True, height=True)

        messages_frame = tkinter.Frame(top)
        my_msg = tkinter.StringVar()
        my_msg.set('')

        scrollbar = tkinter.Scrollbar(messages_frame)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        msg_list = tkinter.Listbox(messages_frame, height=25, width=70, yscrollcommand=scrollbar.set)
        msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        messages_frame.pack()

        entry_field = tkinter.Entry(top, textvariable=my_msg, width=65)
        entry_field.bind('<Return>', enviar_mensagem)
        entry_field.pack()
        entry_field.focus()

        send_button = tkinter.Button(top, text='Enviar', font='Helvetica 10 bold', width=20, command=enviar_mensagem)
        send_button.pack()

        top.protocol('WM_DELETE_WINDOW', fechar_chat)

        #receive_thread = Thread(target=receber_mensagem)
        #receive_thread.start()
        tkinter.mainloop()
    
