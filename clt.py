import threading
import socket 

server=socket.socket(socket.AF_INET,type=socket.SOCK_STREAM)
server.connect((socket.gethostname(),1556))
nickname=input("Enter your nickname:")
def recvs():
    while True:
        try:
            buff=100
            msg=server.recv(buff)
            if msg.decode("utf-8")=="nick":
                server.send(nickname.encode("utf-8"))
            elif "Header" in (msg.decode('utf-8')):
                buffSize=int(msg.decode('utf-8').split(","))
                buff=int(buffSize[1])
                print(buff)
            else:
                # print(msg.decode("utf-8"))
                try:
                    msg=msg.decode("utf-8")
                    msg=msg.split(",")
                    print(f"\n{msg[0]}:{msg[1]}")
                    print(buff)
                    buff=100
                except Exception as IndexError:
                    try:
                        print('\n'+msg.decode('utf-8'))
                    except Exception as e:
                        pass
        except socket.error:
            print(socket.error())
            server.close()
            break


def write():
    while True:
        massage=input(f"{nickname}:")
        server.send((f"{nickname},{massage}").encode("utf-8"))

t1=threading.Thread(target=recvs).start()
t2=threading.Thread(target=write).start()

