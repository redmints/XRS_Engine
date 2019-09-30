import cmd, sys
import socket
import threading
from router import Router

#Instance principale de l'application de test
class Main(cmd.Cmd):
    intro = 'Xeyrus Engine V0.1\n'
    prompt = '>> '

    #Affichage des clients actuellements connectés
    def do_clients(self, args):
        #Demande de la liste des clients (attribut de la classe utils) à la capacité de routage
        print(router.getClients())

if __name__ == '__main__':
    router = Router()
    #Démarrage du thread d'analyse des trames entrantes
    router.start()
    #Instanciation du prompt principal
    Main().cmdloop()
