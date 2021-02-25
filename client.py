"""

Desenvolvedores:
    @AdrlVMA & @MayconCarvalho

-----------------------------------------------------------------------------------------
Classe Cliente - Comunicação RCP
-----------------------------------------------------------------------------------------

Fontes:

"""

import rpyc
import sys

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

host = sys.argv[1]
port = sys.argv[2]

server = rpyc.connect(host, port)
print(server.root)
print(server.root.get_service_name())
print(server.root.get_service_aliases())
print(server.root.fibonnaci(5))
