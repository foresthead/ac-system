import socket
import sys
import pickle


class server:


   def build_server(self):
      conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      return conn


   def listen_from(self, conn, port, host):
      try:
         conn.bind((host, port))
      except:
         print("Bind Failed. Error: " +str(sys.exc_info()))
         sys.exit()
      conn.listen(5)# queue up to 5 request
      print("socket now listening")


   def receive_input(self, conn):
      client_input = conn.recv(1024)
      request = pickle.loads(client_input)
      #print("received")
      return request


   def send_data(self, conn, data):
      response = pickle.dumps(data)
      conn.send(response)
      #print("data sent")


   def closeSocket(self, connection):
      connection.close()


   def connect_to(self, connection, host, port):
       connection.connect((host, port))
