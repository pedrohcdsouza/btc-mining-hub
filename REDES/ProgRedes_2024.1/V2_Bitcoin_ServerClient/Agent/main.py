import socket,sys
from mylib import *

print('THE APPLICATION IS STARTING ...')

# Configuring socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    
    HOST = '127.0.0.1'
    PORT = 31471
    sock.connect((HOST,PORT))

except:

    print('ERROR: THE APPLICATION WAS NOT STARTED ...\n')
    sys.exit()

print('THE APPLICATION WAS STARTED ...\n')

name = str(input('Write a username: '))

startApplication(sock, name) # Calling the primary Function

threading.Thread(target=checkWork, args=(sock,)).start() # Thread to hear server when application is mining