# Catatan TryHackMe — Python Basics

**Sumber belajar:** [TryHackMe: Python Basics](https://tryhackme.com/room/pythonbasics)

Dokumen ini berisi ringkasan materi, contoh kode, penjelasan singkat setiap task, dan flag yang sudah tercatat pada catatan sebelumnya. Flag ditulis sesuai catatan yang tersedia; jika sebuah task belum memiliki flag, bagian tersebut ditandai agar bisa dilengkapi setelah dikerjakan di TryHackMe. Penanda 🟩 digunakan agar baris flag lebih mudah ditemukan saat membaca dokumen.

---

## Task 1 — Introduction to Python

**Materi:** Pengenalan Python dan penggunaan code editor TryHackMe.

Python adalah bahasa pemrograman yang bisa digunakan untuk membuat skrip, mengolah data, dan membantu pekerjaan keamanan siber. Sintaks adalah aturan penulisan kode yang harus diikuti agar program dapat dibaca dan dijalankan dengan benar.

**Yang dilakukan:** Jalankan kode yang sudah tersedia di editor menggunakan tombol **Run Code**, lalu lanjutkan ke task berikutnya.

**Flag:** Tidak ada flag yang tercatat untuk task ini.

---

## Task 2 — Hello World

**Tujuan:** Menampilkan teks ke layar menggunakan `print()`.

**Kode:**
```python
print("Hello World")
```

**Penjelasan:**
- `print()` adalah fungsi untuk menampilkan output.
- `"Hello World"` adalah teks atau string. Teks ditulis di dalam tanda kutip.
- Baris yang diawali `#` merupakan komentar dan tidak dijalankan sebagai kode.

🟩 **FLAG:** `THM{PRINT_STATEMENTS}`

---

## Task 3 — Mathematical Operators

**Tujuan:** Menggunakan operator matematika Python untuk melakukan perhitungan.

| Operasi | Operator | Contoh kode | Hasil | Flag |
|---|---:|---|---:|---|
| Penjumlahan | `+` | `print(21 + 43)` | `64` | `THM{ADDITI0N}` |
| Pengurangan | `-` | `print(142 - 52)` | `90` | `THM{SUBTRCT}` |
| Perkalian | `*` | `print(10 * 342)` | `3420` | `THM{MULTIPLICATION_PYTHON}` |
| Pangkat | `**` | `print(5 ** 2)` | `25` | `THM{EXP0N3NT_POWER}` |

**Penjelasan:**
- `+` menjumlahkan dua nilai.
- `-` mengurangi nilai pertama dengan nilai kedua.
- `*` mengalikan dua nilai.
- `**` menghitung pangkat; `5 ** 2` berarti 5 pangkat 2.
- Operator pembanding yang juga diperkenalkan pada materi ini adalah `>`, `<`, `==`, `!=`, `>=`, dan `<=`. Operator tersebut menghasilkan kondisi benar atau salah dan sering digunakan dalam `if` serta loop.

---

## Task 4 — Variables and Data Types

**Tujuan:** Menyimpan nilai dalam variabel dan memperbarui nilainya.

**Kode:**
```python
height = 200
height = height + 50
print(height)
```

**Penjelasan:**
- `height = 200` membuat variabel `height` dengan nilai awal `200`.
- `height = height + 50` mengambil nilai lama, menambahkan `50`, lalu menyimpan hasilnya kembali ke `height`.
- `print(height)` menampilkan nilai akhir, yaitu `250`.

**Jenis data dasar yang dibahas:**
- **String (`str`)** — teks, misalnya `"ice cream"`.
- **Integer (`int`)** — bilangan bulat, misalnya `2000`.
- **Float (`float`)** — bilangan desimal, misalnya `3.14`.
- **Boolean (`bool`)** — nilai `True` atau `False`.
- **List (`list`)** — kumpulan item, misalnya `["apel", "jeruk"]`.

🟩 **FLAG:** `THM{VARIABL3S}`

---

## Task 5 — Logical and Boolean Operators

**Tujuan:** Memahami operator pembanding dan operator logika untuk memeriksa kondisi.

**Operator pembanding:**

| Operator | Arti | Contoh |
|---|---|---|
| `==` | Sama dengan | `x == 5` |
| `<` | Lebih kecil dari | `x < 5` |
| `<=` | Lebih kecil atau sama dengan | `x <= 5` |
| `>` | Lebih besar dari | `x > 5` |
| `>=` | Lebih besar atau sama dengan | `x >= 5` |

**Operator logika Python:**

| Operator | Kegunaan | Contoh |
|---|---|---|
| `and` | Kedua kondisi harus benar | `x >= 5 and x <= 100` |
| `or` | Minimal satu kondisi benar | `x == 1 or x == 10` |
| `not` | Membalik nilai logika | `not hungry` |

**Contoh kode:**
```python
a = 1

if a == 1 or a > 10:
    print("a is either 1 or above 10")
```

**Penjelasan:** Program menampilkan pesan jika `a` sama dengan `1` atau lebih besar dari `10`. Dalam Python, operator logika ditulis dengan huruf kecil: `and`, `or`, dan `not`.

**Status flag:** Tidak ada flag yang tercatat pada catatan sebelumnya. Halaman TryHackMe meminta pengguna membaca bagian materi ini.

---

## Task 6 — Shipping Project: Introduction to If Statements

**Tujuan:** Menggunakan `if` dan `else` untuk menghitung total belanja beserta biaya pengiriman.

Aturan soal:
- Jika belanja **lebih dari $100**, ongkos kirim gratis.
- Jika belanja **kurang dari atau sama dengan $100**, ongkos kirim adalah `$1.20` per kilogram.

### Soal 1 — Nilai awal

**Kode:**
```python
customer_basket_cost = 34
customer_basket_weight = 44

if customer_basket_cost > 100:
    shipping_cost = 0
else:
    shipping_cost = customer_basket_weight * 1.20

total_cost = customer_basket_cost + shipping_cost

print(total_cost)
```

**Penjelasan:**
- Harga belanja adalah `$34` dan berat keranjang `44 kg`.
- Karena `$34` tidak lebih dari `$100`, biaya kirim adalah `44 × 1.20 = $52.80`.
- Total biaya adalah `$34 + $52.80 = $86.80`.
- Output Python: `86.8`.

🟩 **FLAG:** `THM{IF_STATEMENT_SHOPPING}`

### Soal 2 — Ubah biaya belanja menjadi 101

**Kode:**
```python
customer_basket_cost = 101
customer_basket_weight = 44

if customer_basket_cost > 100:
    shipping_cost = 0
else:
    shipping_cost = customer_basket_weight * 1.20

total_cost = customer_basket_cost + shipping_cost

print(total_cost)
```

**Penjelasan:** Karena `$101` lebih dari `$100`, `shipping_cost` bernilai `0`. Total yang ditampilkan adalah `101`.

🟩 **FLAG:** `THM{MY_FIRST_APP}`

---

## Task 7 — Loops

**Tujuan:** Mengulang instruksi tanpa perlu menulis perintah yang sama berkali-kali.

Python memiliki dua jenis loop yang diperkenalkan di materi ini:
- **`while`** — mengulang selama kondisi masih benar.
- **`for`** — mengulang item pada suatu urutan atau rentang.

**Contoh `while`:**
```python
i = 1
while i <= 10:
    print(i)
    i = i + 1
```

Loop mencetak angka 1 sampai 10. Nilai `i` ditambah satu setiap putaran agar kondisi akhirnya menjadi salah dan loop berhenti.

**Jawaban latihan — tampilkan angka 0 sampai 50:**
```python
for i in range(51):
    print(i)
```

**Penjelasan:** `range(51)` menghasilkan angka dari `0` sampai `50`. Batas akhir `51` tidak ikut dicetak.

🟩 **FLAG:** `THM{L00PS_WHILE_FOR}`

---

## Task 8 — Bitcoin Project: Introduction to Functions

**Tujuan:** Membuat fungsi yang bisa digunakan kembali dan menggabungkannya dengan kondisi `if`.

**Kode:**
```python
def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
    usd_value = bitcoin_amount * bitcoin_value_usd
    return usd_value

bitcoin_amount = 1.2
bitcoin_to_usd = 30000

investment_value = bitcoinToUSD(bitcoin_amount, bitcoin_to_usd)

if investment_value < 30000:
    print("Bitcoin investment is below $30,000!")
else:
    print("Bitcoin investment is at least $30,000.")
```

**Penjelasan:**
- `def` digunakan untuk mendefinisikan fungsi.
- `bitcoin_amount` dan `bitcoin_value_usd` adalah parameter fungsi.
- `usd_value` menghitung jumlah Bitcoin dikalikan harga per Bitcoin.
- `return usd_value` mengembalikan hasil perhitungan.
- `if investment_value < 30000` memeriksa apakah nilai investasi di bawah `$30.000`.

### Soal lanjutan — harga Bitcoin menjadi 24000

Ubah baris berikut:
```python
bitcoin_to_usd = 24000
```

Dengan jumlah Bitcoin `1.2`, nilai investasi menjadi `1.2 × 24000 = 28800`. Karena nilainya kurang dari `$30.000`, program menampilkan peringatan.

🟩 **FLAG:** `THM{BITC0IN_INVESTOR}`

---

## Task 9 — Files

**Tujuan:** Membaca dan menulis file menggunakan Python.

**Kode untuk membaca `flag.txt`:**
```python
f = open("flag.txt", "r")
print(f.read())
f.close()
```

**Penjelasan:**
- `open("flag.txt", "r")` membuka file dalam mode baca (`r`).
- `f.read()` membaca isi file.
- `print()` menampilkan isi file ke layar.
- `f.close()` menutup file setelah selesai digunakan.

Mode file lain yang dijelaskan dalam materi:
- `a` — menambahkan teks ke akhir file.
- `w` — menulis file; membuat file baru jika belum ada dan menimpa isi file jika sudah ada.

🟩 **FLAG:** `THM{F1LE_R3AD}`

---

## Task 10 — Imports

**Tujuan:** Menggunakan library atau modul yang menyediakan fungsi siap pakai.

**Contoh kode dari materi:**
```python
import datetime

current_time = datetime.datetime.now()
print(current_time)
```

**Penjelasan:**
- `import datetime` memuat modul `datetime`.
- `datetime.datetime.now()` mengambil tanggal dan waktu saat ini.
- `print(current_time)` menampilkan hasilnya.
- `pip` adalah pengelola paket Python yang dapat digunakan untuk memasang library tambahan, misalnya `pip install scapy` jika diperlukan dan diizinkan di lingkungan yang digunakan.

**Status flag:** Tidak ada flag yang tercatat pada catatan sebelumnya. Jalankan contoh kode di editor TryHackMe dan ikuti instruksi task untuk menyelesaikannya.

---

## Ringkasan Flag yang Tercatat

| Task | Nama materi | Flag yang tercatat |
|---|---|---|
| 2 | Hello World | `THM{PRINT_STATEMENTS}` |
| 3 | Mathematical Operators — penjumlahan | `THM{ADDITI0N}` |
| 3 | Mathematical Operators — pengurangan | `THM{SUBTRCT}` |
| 3 | Mathematical Operators — perkalian | `THM{MULTIPLICATION_PYTHON}` |
| 3 | Mathematical Operators — pangkat | `THM{EXP0N3NT_POWER}` |
| 4 | Variables and Data Types | `THM{VARIABL3S}` |
| 6 | Shipping Project — nilai awal | `THM{IF_STATEMENT_SHOPPING}` |
| 6 | Shipping Project — belanja 101 | `THM{MY_FIRST_APP}` |
| 7 | Loops | `THM{L00PS_WHILE_FOR}` |
| 8 | Bitcoin Project | `THM{BITC0IN_INVESTOR}` |
| 9 | Files | `THM{F1LE_R3AD}` |

**Catatan:** Flag di atas disalin dari catatan yang diberikan sebelumnya, bukan diverifikasi satu per satu melalui akun TryHackMe. Task 1, Task 5, dan Task 10 belum memiliki flag di catatan tersebut.
