import nmap

def scan_open_ports(target, port_range):
    scanner = nmap.PortScanner()
    scanner.scan(target, port_range)
    open_ports = []

    for host in scanner.all_hosts():
        if scanner[host].state() == "up":
            print(f"Host {host} ({scanner[host].hostname()}):")
            for proto in scanner[host].all_protocols():
                print(f"  Protocol: {proto}")
                lport = scanner[host][proto].keys()
                for port in lport:
                    print(f"    Port: {port}\tState: {scanner[host][proto][port]['state']}")
                    if scanner[host][proto][port]['state'] == 'open':
                        open_ports.append(port)
    return open_ports

def main():
    target = input("Enter the target IP to scan: ")
    port_range = input("Enter the port range to scan (e.g., 20-80): ")

    print(f"\nScanning {target} for open ports...")
    open_ports = scan_open_ports(target, port_range)

    if open_ports:
        print(f"\nOpen ports on {target}: {open_ports}")
    else:
        print(f"\nNo open ports found on {target}.")

if __name__ == "__main__":
    main()

