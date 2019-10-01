import socket
import threading, pickle
from utils import Utils
from client import Client

#Thread d'analyse des trames entrantes pour un client donné
class ClientThread(threading.Thread):

    #Passage de notre toolbox et du client en question en paramètre
    def __init__(self, utils, client):
        threading.Thread.__init__(self)
        self.utils = utils
        self.client = client

    def run(self):
        #Affichage des infos du client
        self.client.print_log("Connexion")

        #Attente des trames entrantes
        while True:
            data = self.client.clientsocket.recv(2048)
            #Désérialization
            trame = pickle.loads(data)
            #Sortie de boucle si la trame est vide (le client s'est déconnecté)
            if trame.payLoad == "" or trame.payLoad == "exit":
                break
            #Affichage de la trame
            self.client.print_log(trame.payLoad)

        #Déconnexion du client
        self.client.print_log("Déconnexion")
        #On l'enlève de la liste des clients actifs
        self.utils.clients.remove(self.client)

class Router(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #Instanciation de la classe Utils pour les opérations globales et le stockage ephemere
        self.utils = Utils()

    def run(self):
        #Déclaration de l'ouverture de la socket
        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpsock.bind(("",1111))

        #Scan des nouveaux clients qui arrivent
        while True:
            tcpsock.listen(10)
            #Connexion d'un client
            (clientsocket, (ip, port)) = tcpsock.accept()
            client = Client(ip, port, clientsocket)
            #Ajout à la liste des clients actifs
            self.utils.clients.append(client)
            #Déclaration du thread du client en question
            newthread = ClientThread(self.utils, client)
            #Puis démarrage de ce dernier
            newthread.start()

    def getClients(self):
        #Retour de la liste des clients actifs
        return self.utils.clients
