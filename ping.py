import os

host = input("Enter IP address or hostname: ")

response = os.system("ping -n 4 " + host)

if response == 0:
    print("Host is reachable")
else:
    print("Host is unreachable")