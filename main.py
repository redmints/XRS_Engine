import cmd, sys
import socket
import threading
from router import Router
from server import Server

#Instance principale de l'application Engine
class Main(cmd.Cmd):
    intro = 'Xeyrus Engine V0.1\n'
    prompt = '>> '
    servers = []


    #Affichage des clients actuellements connectés
    def do_clients(self, args):
        #Demande de la liste des clients (attribut de la classe utils) à la capacité de routage
        print(router.getClients())

    def do_connexion(self, args):
        args = args.split(" ")
        server = Server(args[0], args[1])
        server.start()
        self.servers.append(server)

    def do_send(self, args):
        args = args.split(" ")
        server = self.servers[int(args[0])]
        server.send(args[1])

    def do_deconnexion(self, args):
        args = args.split(" ")
        server = self.servers[int(args[0])]
        server.deconnexion()
        self.servers.pop(int(args[0]))

    def do_servers(self, args):
        print(self.servers)



if __name__ == '__main__':
    router = Router()
    #Démarrage du thread d'analyse des trames entrantes
    router.start()
    #Instanciation du prompt principal
    Main().cmdloop()
