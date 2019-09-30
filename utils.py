class Utils():
    def __init__(self):
        self.clients = []

    def print_log(self, ip, port, message):
        print("["+str(ip)+":"+str(port)+"] "+str(message))

    def remove_client(self, ip, port):
        for i in range(len(self.clients)):
            if self.clients[i][0] == ip and self.clients[i][1] == port:
                self.clients.pop(i)
