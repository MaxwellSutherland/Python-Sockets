import socket
import threading
import JSONmanager as fm
import INImanager as ini

ini.Config_INIT()
fm.InitFiles(ini.GetVariable("SETUP", "log_file"),
              ini.GetVariable("SETUP", "create_file"))

IP              = str()
PORT            = int(ini.GetVariable("SETUP", "port"))
ADDR            = (IP, PORT)
PASSWORD        = str()
SIZE            = 1024
FORMAT          = "utf-8"
DISCONNECT_MSG  = "!DISCONNECT"
SERVER          = None

def CreateServer():
    global      SERVER
    global      PASSWORD
    global      IP
    global      PORT
    PASSWORD    = ini.GetVariable(          "SETUP",      "password")
    IP          = ini.GetVariable(          "SETUP",      "host")
    PORT        = int(ini.GetVariable(      "SETUP",      "port"))
    print("Starting...")
    SERVER      = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind(ADDR)
    SERVER.listen()
    print("Listening...")
    print(f"IP: {IP}. PORT: {PORT}")
    main()

def Login(conn, addr):
    connected = True
    msg             = conn.recv(SIZE).decode(FORMAT)

    if str(msg) == str(PASSWORD):   msg = "1"
    else:                           msg = "0"
    conn.send(msg.encode(FORMAT))
    if msg == "0":
        connected   = False
        conn.close()
    if connected: 
        print(f"New CLIENT connection {addr}")
        if not fm.AlreadyExists(str(addr[0])):fm.CreatePlayer(str(addr[0]))
    return connected

def HandleCLIENT(conn, addr):
    connected       = Login(conn, addr)
    while connected:
        msg             = conn.recv(SIZE).decode(FORMAT)
        tokens          = msg.split(" ")
        print(f"{addr}: {msg}")
        if msg == DISCONNECT_MSG:
            connected   = False
            print(f"CLIENT ({addr[1]}): Disconnected")
        else:
            i           = 0
            for         t in tokens:
                if fm.KeyExists(addr[0], tokens[i]):
                    fm.ChangeData(              str(addr[0]),
                                                tokens[i], 
                                                tokens[i + 1])
                i += 2
                if i >= len(tokens):break

            msg         = f"Recieved {msg}"
        conn.send(msg.encode(FORMAT))
    conn.close()

def main():
    while True:
        conn, addr          = SERVER.accept()
        thread              = threading.Thread(target=HandleCLIENT, 
                                                args=(conn, addr))
        thread.start()

if __name__ == "__main__":CreateServer()