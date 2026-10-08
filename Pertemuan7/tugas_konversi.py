# Menampilkan judul program
print("======================================")
print("       KONVERTER BILANGAN PYTHON      ")
print("======================================")

# Meminta pengguna memasukkan angka desimal
angka = int(input("Masukkan angka desimal: "))

# Menampilkan menu pilihan konversi
print("\nPilih jenis konversi:")
print("1. Biner")
print("2. Hexadesimal")
print("3. Biner dan Hexadesimal")

# Meminta pengguna memilih menu
pilihan = input("Masukkan pilihan (1/2/3): ")

# Mengecek pilihan pengguna
if pilihan == "1":
    # Mengubah angka desimal ke biner menggunakan bin()
    hasil_biner = bin(angka)

    # Menampilkan hasil konversi biner
    print("\nHasil Konversi")
    print("--------------------------------------")
    print(f"Desimal     : {angka}")
    print(f"Biner       : {hasil_biner}")

elif pilihan == "2":
    # Mengubah angka desimal ke hexadesimal menggunakan hex()
    hasil_hexa = hex(angka)

    # Menampilkan hasil konversi hexadesimal
    print("\nHasil Konversi")
    print("--------------------------------------")
    print(f"Desimal     : {angka}")
    print(f"Hexadesimal : {hasil_hexa}")

elif pilihan == "3":
    # Mengubah angka desimal ke biner menggunakan bin()
    hasil_biner = bin(angka)

    # Mengubah angka desimal ke hexadesimal menggunakan hex()
    hasil_hexa = hex(angka)

    # Menampilkan kedua hasil konversi
    print("\nHasil Konversi")
    print("--------------------------------------")
    print(f"Desimal     : {angka}")
    print(f"Biner       : {hasil_biner}")
    print(f"Hexadesimal : {hasil_hexa}")

else:
    # Menampilkan pesan jika pilihan tidak sesuai
    print("\nPilihan tidak valid.")