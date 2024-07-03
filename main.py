import socket
import subprocess
import platform
from colorama import Fore

System = platform.system()
server_ip = input(Fore.BLUE +"Enter your server ip: ")
port = 8888
server_protocol = input("server prtocol TCP or UDP ?").upper()
def server_TCP(server_ip, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, port))
    server_socket.listen()
    print(f"start listening TCP on {server_ip}:{server_port}")
    while True:
        client_socket, client_address = server_socket.accept()
        if System == "Linux":
            subprocess.run('clear', shell=True)
        elif System == "Windows":
            subprocess.run('cls', shell=True)
        print(Fore.WHITE + f"Accepted connection from {client_address[0]}:{client_address[1]}")
        command = client_socket.recv(1024).decode('utf-8')
        print('command:', command)
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print("Output:", result.stdout)
        if result.stderr:
            print("Error:", result.stderr)
        print(Fore.BLUE + f"start listening TCP on {server_ip}:{port}")

def server_UDP(server_ip, server_port):
    server_address = (server_ip, server_port)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(server_address)
    print(f"start listening UDP on {server_ip}:{server_port}")
    while True:
        command = server_socket.recvfrom(4096)
        result = subprocess.run(command[0].decode('utf-8'), shell=True, capture_output=True, text=True)
        print("Output:", result.stdout)
        if result.stderr:
            print("Error:", result.stderr)
        print(f"start listening UDP on {server_ip}:{server_port}")
while True:
    if server_protocol == "TCP":
        server_TCP(server_ip, port)
    elif server_protocol == "UDP":
        server_UDP(server_ip, port)
    else:
        print(Fore.RED + "Invalid protocol. Please enter 'TCP' or 'UDP'.")
