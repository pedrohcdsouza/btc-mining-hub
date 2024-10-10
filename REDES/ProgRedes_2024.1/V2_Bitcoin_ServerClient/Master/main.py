import socket, sys, threading
from mylib import *

print('THE SERVER IS STARTING ...')

# Configuring socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    HOST = '127.0.0.1'
    PORT = 31471
    sock.bind((HOST,PORT))
    sock.listen(10) # Maximum user accepted at one time

except:

    print(f'ERROR: THE SERVER WAS NOT STARTED ...\n')
    sys.exit()

print('THE SERVER WAS STARTED ...\n')

threading.Thread(target=writeTransactions, args=(sock,)).start() # Thread to user Write the transactions
threading.Thread(target=startBot).start() # Thread to Connect the Telegram BOT
while True:
    threading.Thread(target=connectAgents, args=(sock,)).start() # Thread to Connect all agents and hear them