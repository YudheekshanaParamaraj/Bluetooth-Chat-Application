import socket
import threading
import bluetooth

a=None

target_name = "Device"
target_address = None

nearby_devices = bluetooth.discover_devices() #scans devices

for bdaddr in nearby_devices:
if target_name == bluetooth.lookup_name( bdaddr ): #connect to detected
device
target_address = bdaddr
break

if target_address is not None:
print("found target bluetooth device with address ", target_address)
a=True
else:
print("could not find target bluetooth device nearby")
a=False

if a==True:
class ChatServer:
  clients_list = []

last_received_message = ""

def __init__(self):
self.server_socket = None
self.create_listening_server()

def create_listening_server(self):

self.server_socket = socket.socket(socket.AF_INET,
socket.SOCK_STREAM) #create a socket using TCP port and ipv4
local_ip = '127.0.0.1'
local_port = 10319
# restart a TCP server
self.server_socket.setsockopt(socket.SOL_SOCKET,
socket.SO_REUSEADDR, 1)
# this makes the server listen to requests coming from other
computers on the network
self.server_socket.bind((local_ip, local_port))
print("Listening for incoming messages..")
self.server_socket.listen(5) #listen for incomming connections / max 5
clients
self.receive_messages_in_a_new_thread()

def receive_messages(self, so):
while True:
incoming_buffer = so.recv(256) #initialize the buffer
if not incoming_buffer:
  break
self.last_received_message = incoming_buffer.decode('utf-8')
self.broadcast_to_all_clients(so) # send to all clients
so.close()

def broadcast_to_all_clients(self, senders_socket):
for client in self.clients_list:
socket, (ip, port) = client
if socket is not senders_socket:
socket.sendall(self.last_received_message.encode('utf-8'))

def receive_messages_in_a_new_thread(self):
while True:
client = so, (ip, port) = self.server_socket.accept()
self.add_to_clients_list(client)
print('Connected to ', ip, ':', str(port))
t = threading.Thread(target=self.receive_messages, args=(so,))
t.start()
#add a new client
def add_to_clients_list(self, client):
if client not in self.clients_list:
self.clients_list.append(client)

if __name__ == "__main__":
ChatServer()
