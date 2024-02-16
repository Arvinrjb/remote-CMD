import socket
from os import system
import platform
from colorama import Fore

System = platform.system()


def main():
    host = input(Fore.BLUE + "Enter your ip: ")
    port = 8888
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"start listening on {host}:{port}")
    while True:
        client_socket, client_address = server_socket.accept()

        if System == "Linux":
            system('clear')
        elif System == "Windows":
            system('cls')

        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
        command = client_socket.recv(1024).decode()
        system(command)
        print(command)
        client_socket.close()
        print(f"start listening on {host}:{port}")


main()
