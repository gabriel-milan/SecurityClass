import thread
import socket
from simplecrypt import encrypt, decrypt

PATH = "./socket/"
HOST = '192.168.88.133'
PORT = 9000

# Listener
def listener (conn):
    while True:
        income_data = conn.recv(1024)
        if income_data:
            print ("Received: " + decrypt(income_data))

# Sender
def sender (conn):
    while True:
        data = input("> ")
        conn.send(bytes(encrypt(data)))
# Main
def main ():
    # Initialize socket
    print ("Initializing socket...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print ("Connection initialized!")
        try:
            # Start stuff
            thread.start_new_thread (listener, (conn))
            thread.start_new_thread (sender, (conn))
        except:
            print ("Unable to start threads")
        while (True):
            pass

if __name__ == '__main__':
    main()