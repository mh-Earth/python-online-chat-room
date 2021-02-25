import socket,os
import threading

socks=socket.socket(socket.AF_INET,type=socket.SOCK_STREAM)
socks.bind((socket.gethostname(),1555))
socks.listen()
clt_list=[]
nicknames=[]
def addCIT(clt):
    clt_list.append(clt)

def boradcast(msge):
    msge=msge.encode("utf-8")
    for clts in clt_list:
        clts.send(msge)


def recvice():
    while True:
        client,add=socks.accept()
        client.send("nick".encode("utf-8"))
        nickname=client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        addCIT(client)
        boradcast(f"{nickname} join the chat")
        print(f"conncet with {add}")
        print(f"{nickname} join the server")

        thread=threading.Thread(target=heandl,args=(client,))
        thread.start()
        

def heandl(clt):
    while True:
        try:
            massege=clt.recv(2024).decode("utf-8")
            boradcast(msge=massege)
                
        except socket.error:
            index=clt_list.index(clt)
            clt_list.remove(clt)
            nicknames.pop(index)
            boradcast(f"{nickname} left the chat")
            break

recvice()