import socket
import subprocess
import platform
import psutil
from colorama import Fore

ip_list = []
System = platform.system()
port = 8888
local_ping = input(Fore.WHITE + "Can I get a ping from your internal networks? (yes or no) : ")
count = 1
if System.lower() == "windows":
    sys = '-n'
else:
    sys = '-c'

def ping(host):
    process = subprocess.Popen(['ping',sys ,'1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if "Destination host unreachable" not in stdout.decode():
        print(Fore.GREEN + f"ping:{host} good")
        ip_list.append(host)
    elif "Destination host unreachable" in stdout.decode():
        print(Fore.RED + f"ping: {host} bad ")
    else:
        print(Fore.RED + f"ping: {host} bad")

if local_ping.lower() == "yes":

    while count < 255:
        host_ip = f"192.168.1.{count}"
        ping(host_ip)
        count += 1
    print(ip_list)

def get_active_network():
    interfaces = psutil.net_if_addrs()
    for interface_name, interface_addresses in interfaces.items():
        for address in interface_addresses:
            if address.family == socket.AF_INET and not address.address.startswith("127."):
                return interface_name
    return None

def network_info(interface_name):
    interfaces = psutil.net_if_addrs()
    if interface_name in interfaces:
        interface_addresses = interfaces[interface_name]
        for address in interface_addresses:
            if address.family == socket.AF_INET:
                ip = address.address
                print(f"your IP Address:{ip}")
                return ip

def server_TCP(server_ip, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, port))
    server_socket.listen()
    print(f"start listening TCP on {server_ip}:{server_port}")
    while True:
        client_socket, client_address = server_socket.accept()
        if System.lower() == "linux":
            subprocess.run('clear', shell=True)
        elif System.lower() == "windows":
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

server_ip = input(Fore.BLUE +"Enter your server ip automatically or manual (default=automatically): ")
if server_ip.lower() == "manual":
    ip = input("Enter your server ip: ")
else:
    active_network = get_active_network()
    if active_network:
        ip = network_info(active_network)
    else:
        print(Fore.RED + "No active network found.")
        ip = input(Fore.WHITE + "Enter your server ip: ")
server_protocol = input("server prtocol TCP or UDP ?").upper()
while True:
    if server_protocol == "TCP":
        server_TCP(ip, port)
    elif server_protocol == "UDP":
        server_UDP(ip, port)
    else:
        print(Fore.RED + "Invalid protocol. Please enter 'TCP' or 'UDP'.")
