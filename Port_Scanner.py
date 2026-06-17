import socket

target = input("Enter target IP or domain: ")

print("Scanning ports on", target)

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    """AF_INET → IPv4 (normal internet IPs)
    SOCK_STREAM → TCP connection (reliable connection-based protocol)"""
    socket.setdefaulttimeout(0.1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    s.close()

print("Scan completed")