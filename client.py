import pickle

class Client():
    #Constructeur
    def __init__(self, ip, port, clientsocket):
        #Déclaration du tableau des clients actifs
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket

    #Formatage et affichage d'un message client
    def print_log(self, message):
        print("["+str(self.ip)+":"+str(self.port)+"] "+str(message))

    #Envoi d'une trame
    def send(self, trame):
        trame = pickle.dumps(trame)
        self.clientsocket.send(trame)
