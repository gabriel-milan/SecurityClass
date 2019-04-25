import socket
from time import time
from Crypto.Cipher import AES

PATH = "./socket/"
CLIENT = '10.10.11.116'
PORT = 9000
KEY = b"L45P1L45P1L45P12"

# Main
def main ():
    # Initialize socket
    print ("Initializing socket...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((CLIENT, PORT))

    # Decrypt stuff
    decryption_suite = AES.new(KEY, AES.MODE_CBC, 'This is an IV456')

    print ("Connection initialized!")
    while True:
        data = input("> ")
        initial_time = time()
        s.send(bytes(decryption_suite.encrypt(data)))
        print ("Send deltaT: " + str(time() - initial_time))

if __name__ == '__main__':
    main()