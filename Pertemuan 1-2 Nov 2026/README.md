# Tugas Kriptografi Dasar I — AES-256

## Deskripsi

Script `aes256_file.py` menjalankan proses pembuatan kunci, enkripsi file,
dekripsi file, dan verifikasi hasil menggunakan **AES-256-GCM** dari library
Python `cryptography`.

AES-256 menggunakan kunci sepanjang 256 bit (32 byte). Mode GCM memberikan
enkripsi sekaligus pemeriksaan integritas data. File `.enc` berisi penanda
format, nonce, dan ciphertext beserta tag autentikasinya.

## 1. Persiapan

Pastikan Python 3 sudah terpasang. Disarankan menggunakan virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install cryptography
```

Di Windows, aktifkan virtual environment dengan:

```powershell
.venv\Scripts\activate
```

## 2. Siapkan file plaintext

Buat file teks, misalnya `pesan.txt`, lalu isi dengan data yang ingin diuji.

Contoh:

```text
Ini adalah data rahasia untuk pengujian enkripsi AES-256.
```

## 3. Generate AES-256 key

```bash
python aes256_file.py generate-key --key secret.key
```

Key dibuat secara acak dan disimpan di `secret.key`, terpisah dari source code.
Jalankan perintah ini satu kali untuk membuat key. Jangan membuat key baru
sebelum mendekripsi file yang masih menggunakan key lama.

## 4. Enkripsi file teks

```bash
python aes256_file.py encrypt --input pesan.txt --output pesan.enc --key secret.key
```

Hasil enkripsi disimpan sebagai `pesan.enc`.

## 5. Dekripsi file

```bash
python aes256_file.py decrypt --input pesan.enc --output hasil_dekripsi.txt --key secret.key
```

Hasil dekripsi dikembalikan ke file `hasil_dekripsi.txt`.

## 6. Verifikasi hasil

```bash
python aes256_file.py verify --original pesan.txt --decrypted hasil_dekripsi.txt
```

Jika kedua file identik, script menampilkan:

```text
[OK] Verifikasi berhasil: hasil dekripsi IDENTIK dengan file asli.
```

## Lokasi key, risiko kebocoran, dan keamanan production

- **Lokasi penyimpanan:** key berada di file terpisah `secret.key` pada direktori
  kerja (atau lokasi yang ditentukan melalui opsi `--key`). Di Linux/Kali,
  script mencoba membatasi izin file menjadi `600`.
- **Risiko jika bocor:** pihak yang memperoleh key dapat mendekripsi file yang
  dienkripsi dengan key tersebut. Karena itu, jangan mengirim `secret.key`
  bersama file `.enc`, mengunggahnya ke repository publik, atau menaruhnya
  langsung di source code.
- **Untuk production:** gunakan secret manager/KMS atau HSM, batasi akses hanya
  untuk proses dan pengguna yang berwenang, simpan backup key secara terenkripsi,
  lakukan rotasi key dengan prosedur yang benar, dan pantau akses terhadap key.
  Jangan menghapus key lama sebelum semua data yang menggunakannya berhasil
  dimigrasikan atau tidak lagi diperlukan.

## Catatan

- Nonce 12 byte dibuat secara acak untuk setiap proses enkripsi dan disimpan
  bersama ciphertext. Nonce bukan secret, tetapi tidak boleh digunakan ulang
  dengan key yang sama.
- Jika key salah atau isi file terenkripsi berubah/rusak, pemeriksaan autentikasi
  AES-GCM akan menyebabkan dekripsi gagal.
- Simpan file `secret.key` dengan aman. Kehilangan key berarti file terenkripsi
  tidak dapat didekripsi.
