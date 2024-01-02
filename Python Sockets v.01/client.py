import socket
import time

IP              = str()
PORT            = int()
ADDR            = (0, 0)
SIZE            = 1024
FORMAT          = "utf-8"
DISCONNECT_MSG  = "!DISCONNECT"
connected       = True
CLIENT          = None

def Connect():
    global      CLIENT
    global      IP
    global      PORT
    global      ADDR
    global      connected
    print("Enter SERVER IP Address: ", end='')
    IP          = input()
    print("Enter SERVER Port: ", end='')
    PORT        = input()
    ADDR        = (IP, int(PORT))
    CLIENT      = socket.socket(socket.AF_INET, 
                                socket.SOCK_STREAM)
    try:        CLIENT.connect(ADDR)
    except:
        print(f"Failed to connect to ({IP}, {PORT}")
        Connect()
    print("Enter SERVER Password: ", end='')
    password    = input()
    SendMessage(CLIENT, 
                password)
    msg         = CLIENT.recv(SIZE).decode(FORMAT)
    if msg == "1":
        connected = True
        main()
    else: Connect()

def main():
    print(f"Connected to {IP}:{PORT}")
    while connected:
        print('> ', end='')
        msg     = input()
        SendMessage(CLIENT, msg)
        start   = time.time()
        msg     = CLIENT.recv(SIZE).decode(FORMAT)
        end     = time.time()
        print(f"{msg} ({round((end - start) * 1000)}ms)")
    Connect()

def SendMessage(CLIENT, msg):
    global connected
    CLIENT.send(msg.encode(FORMAT))
    if msg == DISCONNECT_MSG: 
        connected = False

if __name__ == "__main__":Connect()    
