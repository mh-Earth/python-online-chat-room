import threading
import socket 
import colorama
server=socket.socket(socket.AF_INET,type=socket.SOCK_STREAM)
server.connect((socket.gethostname(),1555))
nickname=input("Enter your nickname:")
def recvs():
    while True:
        try:
            msg=server.recv(2024)
            if msg.decode("utf-8")=="nick":
                server.send(nickname.encode("utf-8"))
            
            elif f'\033[91m{nickname}\033[91m,' in msg.decode('utf-8'):
                pass

            else:
                # print(msg.decode("utf-8"))
                try:
                    msg=msg.decode("utf-8")
                    msg=msg.split(",")
                    # print(f'msg={msg}')
                    if msg[1]=='\033[97mleave\033[97m':
                        print(f"\033[91m[!]{msg[0]} leave the chat\033[91m")
                    else:
                        print(f"\033[32m{msg[0]}\033[32m:\033[97m{msg[1]}\033[97m")
                except Exception as IndexError:
                    print(f'\033[93m{msg}\033[93m')

        except socket.error:
            print(socket.error())
            server.close()
            break


def write():
    while True:
        massage=input("\033[97m")
        if massage=="leave":
            server.send((f"\033[91m{nickname}\033[91m,\033[97m{massage}\033[97m").encode("utf-8"))
            server.close()
            break
        if massage==" " or massage=="":
            pass
        else:
            server.send((f"\033[91m{nickname}\033[91m,\033[97m{massage}\033[97m").encode("utf-8"))

t1=threading.Thread(target=recvs).start()
t2=threading.Thread(target=write).start()

