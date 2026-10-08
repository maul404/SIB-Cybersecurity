# Port Scanner Sederhana
# Target: localhost (127.0.0.1)

import socket

target = "127.0.0.1"

ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP Alternatif"
}

print("=== PORT SCANNER ===")
print(f"Target: {target}")
print("-" * 40)

hasil = []

for port, service in ports.items():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        status = f"Port {port}: OPEN ({service})"
    else:
        status = f"Port {port}: CLOSED"

    print(status)
    hasil.append(status)

    s.close()

print("-" * 40)
print("Scan selesai!")

# Menyimpan hasil ke file
with open("hasil_scan.txt", "w") as file:
    file.write("=== HASIL PORT SCANNER ===\n")
    file.write(f"Target: {target}\n")
    file.write("-" * 40 + "\n")

    for hasil_port in hasil:
        file.write(hasil_port + "\n")

    file.write("-" * 40 + "\n")
    file.write("Scan selesai!\n")

print("Hasil scan disimpan ke hasil_scan.txt")