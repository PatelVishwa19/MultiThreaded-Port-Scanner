import socket
import threading
from datetime import datetime

COMMON_SERVICES = {
    21: "ftp",
    22: "ssh",
    23: "telnet",
    25: "smtp",
    53: "dns",
    80: "http",
    110: "pop3",
    143: "imap",
    443: "https",
    8080: "http-alt",
    3306: "mysql",
    3389: "rdp"
}


target = input("\nEnter Target IP Address: ")
start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))

print("\nScan started at:", datetime.now())

open_ports = []
lock = threading.Lock()

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))
        if result == 0:
            service = COMMON_SERVICES.get(port)
            if service is None:
                try:
                    service = socket.getservbyport(port, "tcp")
                except:
                    service = "Unknown"

            try:
                sock.send(b"GET / HTTP/1.1\r\nHost: test\r\n\r\n")
                banner = sock.recv(1024).decode(errors="ignore").strip()
                if banner == "":
                    banner = "No banner received"
            except:
                banner = "Banner grab failed"

            output = f"Port {port} OPEN | Service: {service} | Banner: {banner}"

            with lock:
                open_ports.append(output)
                print(output)

        sock.close()
    except:
        pass

threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

with open("scan_results.txt", "w") as file:
    for result in open_ports:
        file.write(result + "\n")

print("\nScan completed at:", datetime.now())
print("Results saved in scan_results.txt")
