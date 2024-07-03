import socket
import platform
import os
from colorama import Fore

System = platform.system()
if System == "Linux":
    os.system('clear')
elif System == "Windows":
    os.system('cls')
print(Fore.GREEN + f"You are using operating system: {System}")
server_address = input(Fore.GREEN + "Enter your ip server: ")  
server_port = 8888  

def send_command_TCP(address, port, command):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((address, port))
        client_socket.send(command.encode('utf-8'))
    except Exception as error:
        print(Fore.RED + "Error:", error)
    finally:
        client_socket.close()

def send_command_UDP(address, port, command):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        client_socket.sendto(command.encode('utf-8'), (address, port))
    except Exception as error:
        print(Fore.RED + "Error:", error)
    finally:
        client_socket.close()

while True:
    command_to_send = input(Fore.WHITE + "Enter your command ('E': Exit): ")
    if command_to_send.upper() == 'E':
        exit()
    protocol = input("Server protocol (TCP or UDP): ").upper()
    if protocol == "TCP":
        send_command_TCP(server_address, server_port, command_to_send)
    elif protocol == "UDP":
        send_command_UDP(server_address, server_port, command_to_send)
    else:
        print(Fore.RED + "Invalid protocol. Please enter 'TCP' or 'UDP'.")
