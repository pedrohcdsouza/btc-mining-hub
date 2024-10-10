import threading, struct, time, sys, hashlib, datetime

# STATIC VARIABLES

threadLock = threading.Lock()

# DYNAMIC VARIABLES

checkwork = False

def checkWork(sock):

    global checkwork
    while checkwork:

        protocol = sock.recv(1)

        if protocol == b'I':
            print('NONCE JA FOI ENCONTRADO!')
            checkwork = False
            _ = sock.recv(2)
        
        elif protocol == b'Q':
            print('THE SERVER WAS CLOSED ...\n')
            sys.exit()
        
        else:
            print('ERROR: SOMETHING WRONG WITH SERVER/CLIENT COMMUNICATION ...\n')
            sys.exit()

def startMining(sock):

    startTime = datetime.datetime.now()

    response = sock.recv(13)
    while len(response) != 13:
        response += sock.recv(1)

    numT, numA, winS, bits, size = struct.unpack('!HHIBI', response)

    trans = sock.recv(size)
    while len(trans) != size:
        trans += sock.recv(1)
    
    global checkwork
    checkwork = True

    while checkwork:
        if numA == 1:
            nonce = 0
        else:
            nonce = winS
        print(f'SEARCHING TRANS {numT}...\n\n')
        while nonce < winS*numA -1:
            print(nonce)
            bValue = struct.pack('!I', nonce)
            hashx = hashlib.sha256(bValue + trans).digest()
            binario = ''.join(format(byte, '08b') for byte in hashx)
            
            if binario[:bits] == '0' * bits:

                response = struct.pack('!cHi', b'S', numT, nonce)
                sock.sendall(response)
                break
            
            nonce += 1
        
        with threadLock:
            
            protocol = sock.recv(1)

            if protocol == b'A':
                nowTime = datetime.datetime.now()
                print(f'TRANS {numT}\nNONCE: {nonce} ACCEPTED on {nowTime-startTime}\n\n')
                _ = sock.recv(2)
                _ = sock.recv(3)
            elif protocol == b'R':
                print(f'TRANS {numT}\nNONCE: {nonce} REJECTED on {nowTime-startTime}\n\n')
                _ = sock.recv(2)
            elif protocol == b'Q':
                print('THE SERVER WAS CLOSED ...\n\n')
                time.sleep(15)
                sys.exit()
            elif protocol == b'I':
                print('NONCE JA FOI ENCONTRADO')
                _ = sock.recv(2)
                print(f'')
            else:
                print('ERROR: SOMETHING WRONG WITH SERVER/CLIENT COMMUNICATION ...\n\n')
                sys.exit()

            checkwork = False

def startApplication(sock, name):

    while True:

        if isinstance(name, str):
            name = name.encode('utf-8')

        request = struct.pack('!c10s', b'G', name)
        sock.sendall(request)

        protocol = sock.recv(1)

        if protocol == b'W':
            print('NO TRANSACTION\nWAITING ...\n\n')
            time.sleep(10)
        
        elif protocol == b'Q':
            print('THE SERVER WAS CLOSEDn\n\n')
            sys.exit()
        
        elif protocol == b'T':
            startMining(sock)
        
        else:
            print('ERROR: SOMETHING WRONG WITH SERVER/CLIENT COMMUNICATION\n\n')
            sys.exit()