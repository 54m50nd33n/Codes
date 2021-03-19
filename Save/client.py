import socket
import os
import sys
import re

ip_fam = socket.AF_INET
prot = socket.SOCK_STREAM

def connection(host, port):
    s = socket.socket(ip_fam, prot)
    s.connect((host, port))
    req = b'/mynav'
    s.send(req)
    data = s.recv(1000000)
    dta = data.decode()
    return dta


def read_data():
    cn = connection("localhost", 4444)
    with open("notmynav.html", "w") as f:
        dt = f.write(cn)

connection("localhost", 4444)
