#!/usr/bin/env python
import socket
import subprocess
import sys

# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
remoteServerIP  = raw_input("Enter IP: ")

# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Please wait, scanning remote host", remoteServerIP
print "-" * 60

# We also put in some error handling for catching errors

try:
    for port in range(500,501):  
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.settimeout(2)
        try:
            s.connect((remoteServerIP, port))
            s.send(b'Respond True')
            result = s.recv(1024)
            if result:
                print "Port {}: Result: {}".format(port, result)
            else:
                print "Port {}: No response.".format(port)
            s.close()   
        except socket.error:
            print "Couldn't connect to port {}".format(port)
            pass

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()