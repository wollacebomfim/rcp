import socket

class CRH_TCP:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def send(self, msg):
        self.socket.send(msg)

    def receive(self):
        return self.socket.recv(1024)

    def close(self):
        self.socket.close()

class CRH_UDP:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = (host, port)

    def send(self, msg):
        self.socket.sendto(msg, self.server_address)

    def receive(self):
        data, _ = self.socket.recvfrom(1024)
        return data

    def close(self):
        self.socket.close()

class SRH_TCP:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen(1)
        self.conn, _ = self.socket.accept()

    def send(self, msg):
        self.conn.send(msg)

    def receive(self):
        return self.conn.recv(1024)

    def close(self):
        self.conn.close()
        self.socket.close()

class SRH_UDP:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = (host, port)
        self.socket.bind(self.server_address)
    def send(self, msg):
        self.socket.sendto(msg, self.server_address)

    def receive(self):
        data, _ = self.socket.recvfrom(1024)
        return data

    def close(self):
        self.socket.close()


# Servidor
def server():
    srh = SRH_TCP("localhost", 12345)
    while True:
        data = srh.receive()
        if not data:
            break
        print("Servidor para Cliente:", data.decode())
        srh.send(b"Mensagem Enviada")

    srh.close()

# Cliente
def client():
    crh = CRH_TCP("192.168.0.101", 12345)
    message = b"Ola Servidor foi enviado uma msg para voce"
    crh.send(message)
    response = crh.receive()
    print("Cliente para Servidor:", response.decode())
    crh.close()

if __name__ == "__main__":
    import threading

    # Inicie o servidor em uma thread separada
    server_thread = threading.Thread(target=server)
    server_thread.start()

    # Inicie o cliente no programa principal
    client()git 


