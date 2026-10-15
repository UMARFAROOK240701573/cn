import socket

s = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                   socket.IPPROTO_IP)

host = socket.gethostbyname(socket.gethostname())
s.bind((host, 0))
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

print("Packet Sniffer Started")

try:
    while True:
        packet, addr = s.recvfrom(65535)
        print("Source IP:", addr[0])
        print("Packet Size:", len(packet))

except KeyboardInterrupt:
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    s.close()
    print("Sniffer stopped")