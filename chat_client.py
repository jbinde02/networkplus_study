import socket
import threading
import re

def create_tcp_connection(ip, port):
    s = socket.socket()
    s.connect((ip, port))
    x = s.recv(4096)
    print(x.decode())

    t1 = threading.Thread(target=handle_sends, args=[s], daemon=True)
    t2 = threading.Thread(target=handle_recvs, args=[s], daemon=True)
    print("System: Starting send thread")
    t1.start()
    print("System: Starting receive thread")
    t2.start()

    t1.join()
    print("system: Both threads are closed")
    
    
def handle_sends(sock):
    print("System (Send thread): Type in a message")
    while True:
        msg = input()
        sock.send(bytes(msg, "utf-8"))
        # print("System: Message sent")
        if msg == "Goodbye":
            sock.close()
            break


def handle_recvs(sock):
    p = r"^\$\!\@(.*)\@\!\$(.*)$"
    while True:
        x = sock.recv(4096)
        if x:
            y = x.decode()
            msg = re.findall(p, x.decode())[0]
            # print(f"System (Receive thread): Message received from {msg[0]} - {msg[1]}")
            print(f"{msg[0]} - {msg[1]}")




if __name__ == "__main__":
    create_tcp_connection(input("IP address?"), 12345)