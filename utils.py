class Utils():
    #Constructeur
    def __init__(self):
        #Déclaration du tableau des clients actifs
        self.clients = []

    #Formatage et affichage d'un message client
    def print_log(self, ip, port, message):
        print("["+str(ip)+":"+str(port)+"] "+str(message))

    #Suppression d'un client dans le tableau (déconnexion d'un client)
    def remove_client(self, ip, port):
        for i in range(len(self.clients)-1):
            if self.clients[i][0] == ip and self.clients[i][1] == port:
                self.clients.pop(i)
