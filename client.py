import socket
import platform
from os import system
from colorama import Fore

System = platform.system()

if System == "Linux":
    system('clear')
elif System == "Windows":
    system('cls')

print(Fore.GREEN + f"You are using operating system:{System}")
server_host = input("Enter Host ip: ")
server_port = 8888


def send_command(host, port, command):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        client_socket.send(command.encode())
    except Exception as error:
        print("Error:", error)
    finally:
        client_socket.close()


while True:
    command_to_send = input("Enter your command('e':exit): ")
    if command_to_send.lower() == 'e':
        break
    send_command(server_host, server_port, command_to_send)
