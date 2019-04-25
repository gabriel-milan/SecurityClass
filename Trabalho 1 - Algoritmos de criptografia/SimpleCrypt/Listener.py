import socket
from time import time
from simplecrypt import encrypt, decrypt

PATH = "./socket/"
HOST = '10.10.11.116'
PORT = 9000
KEY = "L45P1"

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
        while True:
            income_data = conn.recv(1024)
            start_time = time()
            if income_data:
                print ("Received: " + decrypt(KEY, income_data).decode('utf-8'))
                print ("Receive deltaT: " + str(time() - start_time))

if __name__ == '__main__':
    main()