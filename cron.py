#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ./cron.py <host> <porta>
# exemplo de uso 
# ./cron.py 127.0.0.1 80
import sys
import socket
from contextlib import closing
def ping(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)                                      
    result = sock.connect_ex((str(host), int(port) ))
    if result == 0:
        print '1'
    else:
        print '0'
ping(sys.argv[1], sys.argv[2])



