#coding=utf-8

from socket import *
from multiprocessing import Process
import re

HTML_ROOT_DIR = "./HTML"
def main():
    server = socket(AF_INET,SOCK_STREAM)
    server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    server.bind(("",7777))
    server.listen(128)

    while True:
        client_socket, clientInfo = server.accept()
        print("[%s:%s]"%(clientInfo))
        handle_client = Process(target=respond,args=(client_socket,))
        handle_client.start()
        client_socket.close()

def respond(client_socket):
    recvData = client_socket.recv(1024)
    print("request data :%s"%recvData)
    recv_lines = recvData.splitlines()
    # for line in recv_lines:
    #         print(line)
    recv_start_line =recv_lines[0];
    resource_name=re.match(r"\w+ +(/[^ ]*) ",recv_start_line.decode("utf-8")).group(1)

    try:
        #尝试打开
        file = open(HTML_ROOT_DIR+resource_name,"rb")

    except IOError:
        #遇到异常
        respond_start_line = "HTTP/1.1 404 not found\r\n"
        respond_headers = "Server : King server\r\n"
        respond_body = "the file is not found"
    else:
        #未遇到异常
        file_data = file.read()
        file.close()

        respond_start_line = "HTTP/1.1 200 OK\r\n"
        respond_headers = "Server : King server\r\n"
        respond_body = file_data.decode("utf-8")
    finally:

        respones = respond_start_line + respond_headers + "\r\n" + respond_body

    print("respones data :%s" % respones)

    client_socket.send(bytes(respones, "utf-8"))

    client_socket.close()




if __name__=="__main__":
        main()