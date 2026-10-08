# Password Strength Checker Enhanced

password = input("Masukkan password: ")

score = 0
saran = []

# Cek panjang password
if len(password) >= 12:
    score += 25
else:
    saran.append("Saran: Gunakan password minimal 12 karakter.")

# Cek huruf besar
if any(char.isupper() for char in password):
    score += 20
else:
    saran.append("Saran: Tambahkan minimal satu huruf besar.")

# Cek huruf kecil
if any(char.islower() for char in password):
    score += 20
else:
    saran.append("Saran: Tambahkan minimal satu huruf kecil.")

# Cek angka
if any(char.isdigit() for char in password):
    score += 15
else:
    saran.append("Saran: Tambahkan minimal satu angka untuk meningkatkan keamanan.")

# Cek simbol
simbol = "!@#$%^&*"

if any(char in simbol for char in password):
    score += 20
else:
    saran.append("Saran: Tambahkan minimal satu simbol (!@#$%^&*).")

# Menentukan kategori
if score >= 80:
    kategori = "KUAT"
elif score >= 50:
    kategori = "SEDANG"
else:
    kategori = "LEMAH"

# Menampilkan hasil
print("\n=== PASSWORD STRENGTH CHECKER ===")
print(f"Skor Password : {score}/100")
print(f"Kategori       : {kategori}")

# Menampilkan saran
if saran:
    print("\nSaran:")
    for item in saran:
        print("-", item)
else:
    print("\nPassword sudah memenuhi semua kriteria keamanan.")