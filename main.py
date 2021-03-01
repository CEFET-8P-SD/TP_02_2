from tkinter import *
import os


class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("Login usando RPC")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300)

        self.pls = Label(self.login, text="Digite endereço IP", font=("Arial", 16), justify=CENTER)
        self.pls.place(relheight=0.1, relx=0.15, rely=0.1)

        self.labelIp = Label(self.login, text="IP: ")
        self.labelIp.place(relheight=0.1, relx=0.2, rely=0.2)

        self.entryIP = Entry(self.login)
        self.entryIP.place(relwidth=0.5, relheight=0.10, relx=0.30, rely=0.2)
        self.entryIP.focus()

        self.pls2 = Label(self.login, text="Digite seu nome", font=("Arial", 16), justify=CENTER)
        self.pls2.place(relheight=0.1, relx=0.15, rely=0.35)

        self.labelName = Label(self.login, text="Nome: ")
        self.labelName.place(relheight=0.1, relx=0.2, rely=0.45)

        self.entryName = Entry(self.login)
        self.entryName.place(relwidth=0.5, relheight=0.10, relx=0.30, rely=0.45)

        self.go = Button(self.login,
                         text="CONTINUE",
                         command=lambda: self.init_chat(self.entryIP.get(), self.entryName.get()))
        self.go.place(relx=0.4, rely=0.70)

        self.Window.mainloop()

    def init_chat(self, ip, name):
        if ip == "" or ip is None or name == "" or name is None:
            return

        self.login.destroy()
        os.system("python3 client.py " + ip + " " + name)


if __name__ == '__main__':
    g = GUI()
