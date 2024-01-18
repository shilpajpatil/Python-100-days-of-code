

import socket

def cal():
    #get local host name
    local_host = socket.gethostname()

    #list of ip addressess
    ip_add = socket.gethostbyname(local_host)[2]

    #filter out loopback address
    filter_ips = [ip for ip in ip_add if not ip.startswith("127.")]

    # Extract first ip address
    first_ip = filter_ips[:1]

    print(first_ip[0])