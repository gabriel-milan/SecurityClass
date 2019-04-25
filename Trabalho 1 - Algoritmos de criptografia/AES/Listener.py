import socket
from time import time
from Crypto.Cipher import AES

PATH = "./socket/"
HOST = '10.10.11.116'
PORT = 9000
KEY = b"L45P1L45P1L45P12"

# Main
def main ():
    # Initialize socket
    print ("Initializing socket...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)

    # Decrypt stuff
    decryption_suite = AES.new(KEY, AES.MODE_CBC, 'This is an IV456')

    conn, addr = s.accept()
    with conn:
        print ("Connection initialized!")
        while True:
            income_data = conn.recv(1024)
            start_time = time()
            if income_data:
                print ("Received: " + decryption_suite.decrypt(income_data).decode('utf-8'))
                print ("Receive deltaT: " + str(time() - start_time))

if __name__ == '__main__':
    main()