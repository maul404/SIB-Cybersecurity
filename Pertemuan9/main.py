from security_utils import generate_random_password
from security_utils import is_valid_ip
from security_utils import bytes_to_human


# Generate password
password = generate_random_password()
print("Password acak :", password)

# Validasi IP
ip = input("Masukkan alamat IP : ")

if is_valid_ip(ip):
    print("Alamat IP valid")
else:
    print("Alamat IP tidak valid")

# Konversi bytes
bytes_value = int(input("Masukkan jumlah bytes : "))
print("Ukuran :", bytes_to_human(bytes_value))