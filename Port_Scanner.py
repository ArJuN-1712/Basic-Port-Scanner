import sys
import socket
from datetime import datetime as dt

# Check if the correct number of arguments are passed
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid argument! Syntax: python3 Port_Scanner.py <ip>")
    sys.exit()

print("*" * 50)
print("Scanning Target: " + target)
print("Date and Time: {}".format(dt.now()))
print("*" * 50)

try:
    # Scan ports from 50 to 85
    for port in range(50, 86):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET=IPV4 address family, SOCK_STREAM=stream of data
        s.settimeout(1)  # Set a timeout of 1 second
        res = s.connect_ex((target, port))  # Returns 0 signifying a successful connection and an open port
        if res == 0:
            print("Successful Connection | Open Port: {}".format(port))
        s.close()  # Close the socket connection
except KeyboardInterrupt:
    print("\nExiting Program")
except socket.gaierror:
    print("\nHostname could not be resolved")
except socket.error:
    print("\nCould not connect to server") 
