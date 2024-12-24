import socket
import time
import threading
import random
import datetime


def start_server(ip, port):
    sock = socket.create_server((ip, port))
    sock.listen()
    print("Begin listening thread...")
    accept_thread = threading.Thread(target=accept_connections, args=[sock, (ip,port)])
    accept_thread.start()
    accept_thread.join()
    print("Shutting down server")
    

socket_list = []
def accept_connections(sock, address):
    while True:
        client_socket, client_address = sock.accept()
        print(client_socket,client_address)
        socket_list.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=[client_socket, client_address, (address[0],address[1])])
        client_thread.start()
        client_thread.join()
        print(f"Connection closed with client {client_address}.")
        socket_list.remove(client_socket)


def handle_client(client_socket, client_address, server_address):
    client_socket.send(bytes(f"Hear you loud and clear from {server_address[0]}:{server_address[1]}\nGo ahead and start chatting", "utf-8"))
    with open("communications.txt", "at", buffering=1) as f:
        while True:
            x = client_socket.recv(4096)
            if not x:
                print("No data from client. Closing connection.")
                client_socket.close()
                break
            else:
                msg = x.decode()
                dt = datetime.datetime.now()
                print(f"Message received from {client_address} at {dt}")
                f.write(f"{dt} - {client_address}: " + msg)
                f.write("\n")
                send_message_to_other_clients(client_socket, msg)
                if msg == "Goodbye":
                    break
    


def send_message_to_other_clients(client_sock, message):
    for sock in socket_list:
        if sock == client_sock:
            continue
        else:
            message = f"$!@{client_sock.getpeername()}@!$ {message}"
            sock.send(bytes(message, "utf-8"))



server_listening_ip = "0.0.0.0"
server_port = 12345
if __name__ == "__main__":
    start_server(server_listening_ip, server_port)

