import socket
from datetime import datetime
import ipaddress

def scan_port(ipaddress, port):
    try:
        with socket.create_connection((ipaddress, port), timeout=10) as sock:
            print(f'[+] Port {port} Opened on {ipaddress}')
    except (socket.error, socket.timeout):
        pass

def scan(target, ports):
    print(f'\nStarting scan for {target}')
    for port in range(1, ports):
        scan_port(target, port)

def scan_ip_range(ip_range, ports):
    try:
        ip_network = ipaddress.IPv4Network(ip_range, strict=False)
        for ip_address in ip_network.hosts():
            scan(str(ip_address), ports)
    except ValueError as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    start = datetime.now()

    targets = input('[*] Enter targets to scan (split by "," or "-"): ')
    ports = int(input('[*] Enter how many ports you want to scan: '))

    if '-' in targets:
        print('[*] Scanning IP range')
        start_ip, end_ip = targets.split('-')
        scan_ip_range(f"{start_ip.strip()}-{end_ip.strip()}", ports)
    elif ',' in targets:
        print('[*] Scanning multiple targets')
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(), ports)
    else:
        scan(targets, ports)

    ends = datetime.now()
    print(f'\n<Time: {ends - start}>')
    input('Press ENTER to exit ...')