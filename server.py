import threading, socket, pickle
from trame import Trame

class Server(threading.Thread):
    def __init__(self, parIp, parPort):
        threading.Thread.__init__(self)
        self.ip = parIp
        self.port = parPort

    def run(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip, int(self.port)))
        print("Connecté")

    def send(self, message):
        trame = Trame(2, 1, message)
        trame = pickle.dumps(trame)
        self.s.send(trame)

    def deconnexion(self):
        self.s.close()
        print("Déconnecté")
