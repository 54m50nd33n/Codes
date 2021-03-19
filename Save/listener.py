import socket
import os
import sys
import re

path = b"/data/data/com.termux/files/home/save/mynav.html"

ip_fam = socket.AF_INET
prot = socket.SOCK_STREAM

def sock(host, port):
    s = socket.socket(ip_fam, prot)
    s.bind((host, port))
    s.listen()
    conn, address = s.accept()
    data = conn.recv(10000000).decode()
    print(data)
    headers = data.split("\n")
    filename = headers[0].split()[1]
    if filename == "/":
        filename = "/mynav.html" 
        with open(path, "r") as f:
            fd = f.read()
            conn.sendall(b"HTTP/1.1\n\n"+fd.encode())
    s.close()

sock("localhost", 4444)
