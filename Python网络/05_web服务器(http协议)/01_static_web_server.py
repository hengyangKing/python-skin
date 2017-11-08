#coding=utf-8

from socket import *
from multiprocessing import Process


def main():
    server = socket(AF_INET,SOCK_STREAM)
    server.bind(("",7788))
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
    respond_start_line = "HTTP/1.1 200 OK\r\n"
    respond_headers = "Server : King server\r\n"
    respond_body = "hello world"
    respones = respond_start_line + respond_headers +"\r\n"+ respond_body
    print("respones data :%s"%respones)

    client_socket.send(bytes(respones,"utf-8"))
    client_socket.close()
    #提取请求方式
    #提取请求数据
    #返回响应数据
    try:
        file = open("../HTML"+"index.html")
        fileData = file.read()
        file.close()
        print(fileData)
    except:
        print("foo")


if __name__=="__main__":
        main()