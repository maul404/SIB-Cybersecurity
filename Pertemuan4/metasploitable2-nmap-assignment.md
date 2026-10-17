# Tugas Lab: Pemindaian Metasploitable2 dengan Nmap

## Tujuan

Peserta menyiapkan jaringan lab terisolasi di VirtualBox, menemukan IP Metasploitable2, melakukan pemindaian port dan service secara bertahap, lalu menyusun laporan risiko berdasarkan bukti hasil scan.

## Batas dan aturan lab

- Target yang diizinkan hanya VM **Metasploitable2** milik lab ini.
- Gunakan jaringan **Host-only** yang dibuat khusus untuk latihan. Jangan gunakan **Bridged Adapter** atau subnet Wi-Fi/LAN kampus/rumah.
- Jangan menambahkan adapter NAT ke Metasploitable2. Jika Kali perlu internet untuk update, lakukan sebelum latihan, lalu nonaktifkan adapter NAT sebelum mulai scan.
- Jangan menjalankan scan terhadap host lain pada jaringan Host-only. Host discovery hanya untuk mengenali perangkat; semua pemindaian lanjutan harus diarahkan ke IP Metasploitable2.
- Ambil snapshot Metasploitable2 sebelum pemindaian. `--script vuln` dapat menjalankan pemeriksaan aktif dan beberapa NSE script berpotensi membebani atau mengganggu service.
- Jangan mencoba login, brute force, mengambil file, membuat shell, atau mengubah sistem target. Tugas ini hanya mencakup pemindaian dan analisis.

## A. Siapkan jaringan VirtualBox

1. Matikan kedua VM sebelum mengubah pengaturan adapter.
2. Di VirtualBox buka **Tools → Network Manager → Host-only Networks**, lalu klik **Create**. Pada beberapa sistem, Network Manager berada di **File → Tools**.
3. Buat satu jaringan Host-only, misalnya `vboxnet0`. Contoh konfigurasi IPv4:
   - Alamat adapter Host-only di host: `192.168.56.1`
   - Network mask: `255.255.255.0` (`/24`)
   - DHCP: aktif
   - DHCP server: `192.168.56.100`
   - Rentang alamat DHCP: `192.168.56.101`–`192.168.56.200`

   Nilai di atas adalah contoh. Jika rentang tersebut bertabrakan dengan jaringan host, pilih subnet privat lain yang tersedia dan gunakan subnet itu secara konsisten.

4. Pada **Kali → Settings → Network → Adapter 1**:
   - centang **Enable Network Adapter**;
   - pilih **Attached to: Host-only Adapter**;
   - pilih jaringan yang baru dibuat, misalnya `vboxnet0`;
   - biarkan **Promiscuous Mode: Deny**.
5. Ulangi pengaturan yang sama pada **Metasploitable2**. Pastikan kedua VM memakai jaringan Host-only yang sama. Jangan memilih Bridged Adapter.
6. Pastikan Kali dan Metasploitable2 memperoleh alamat IP pada subnet tersebut. Catat MAC address Metasploitable2 dari VirtualBox agar bisa membedakan target dari antarmuka host.
7. Buat snapshot Metasploitable2 sebelum memulai pemindaian.

Gambaran koneksi:

```text
Kali (Host-only) ───── vboxnet0 / subnet lab ───── Metasploitable2 (Host-only)
                               │
                         Host fisik VirtualBox

Tidak ada Bridged Adapter. Metasploitable2 tidak memakai NAT.
```

## B. Temukan alamat target

Di Kali, lihat alamat dan rute jaringan:

```bash
ip -br -4 addr
ip route
```

Gunakan rentang subnet Host-only yang terlihat di Kali. Contoh berikut berlaku hanya jika jaringan lab memang `192.168.56.0/24`:

```bash
sudo nmap -sn 192.168.56.0/24 -oA 00-host-discovery
```

Host discovery dapat menampilkan Kali dan alamat adapter host selain Metasploitable2. Cocokkan IP kandidat dengan MAC address VM atau informasi konsol Metasploitable2. Catat IP target, lalu tetapkan variabel berikut. Ganti contoh IP dengan hasil aktual:

```bash
TARGET=192.168.56.101
```

Jika target tidak terlihat, periksa bahwa kedua VM berjalan, memakai adapter Host-only yang sama, dan alamatnya berada pada subnet yang sama. Jangan memperluas scan ke jaringan selain subnet lab yang ditetapkan.

## C. Jalankan pemindaian bertahap

Jalankan perintah dari Kali. Simpan output agar hasil bisa diperiksa dan dilampirkan ke laporan.

### 1. Seribu port populer dan deteksi versi

```bash
sudo nmap -sV --top-ports 1000 "$TARGET" -oA 01-top1000-version
```

### 2. Skrip default Nmap

```bash
sudo nmap -sC --top-ports 1000 "$TARGET" -oA 02-default-scripts
```

`-sC` setara dengan menjalankan kategori NSE `default`. Catat informasi tambahan yang relevan dan nama skrip yang menghasilkannya.

### 3. Seluruh port TCP

```bash
sudo nmap -p- -T3 --open "$TARGET" -oA 03-all-tcp
```

`-p-` memeriksa port TCP 1–65535. `--open` membatasi tampilan hasil ke port yang terbuka. Catat daftar port terbuka.

### 4. Deteksi kerentanan pada port terbuka

Ganti contoh daftar port di bawah dengan **seluruh port terbuka yang ditemukan pada tahap 3**:

```bash
sudo nmap -sV --script vuln -p 21,22,23,80,139,445,3632 "$TARGET" -oA 04-vuln
```

Sebelum menjalankan tahap ini, pastikan target masih IP Metasploitable2 dan snapshot tersedia. Kategori `vuln` memeriksa kerentanan tertentu; hasilnya perlu dianalisis dan bukan jaminan bahwa semua kerentanan ditemukan. Sebagian NSE script dapat bersifat intrusif atau mengganggu service. Detail kategori dan perilaku NSE dijelaskan dalam [dokumentasi resmi Nmap](https://nmap.org/book/nse-usage.html).

## D. Isi laporan

Cantumkan:

1. Nama peserta, tanggal, versi Kali/Nmap, subnet Host-only, dan IP target.
2. Perintah yang dijalankan dan file output Nmap (`.nmap`, `.gnmap`, `.xml`).
3. Semua port terbuka beserta protokol, nama service, dan versi yang terdeteksi. Gunakan tabel:

   | Port/protokol | Service | Versi terdeteksi | Bukti/output |
   |---|---|---|---|
   |  |  |  |  |

4. Analisis minimal tiga service paling berisiko. Untuk tiap service, sebutkan bukti dari output scan, dampak yang mungkin, tingkat keyakinan, dan alasan urutan risikonya. Bedakan hasil yang terdeteksi langsung oleh NSE dari risiko yang hanya disimpulkan dari versi/banner.
5. Jika output vuln script hanya mengonfirmasi kurang dari tiga service, tuliskan jumlah yang benar-benar terkonfirmasi. Lengkapi analisis risiko dengan kandidat dari versi/service scan dan beri label **belum terverifikasi**. Jangan mengarang hasil atau menganggap banner saja sebagai bukti eksploitasi.
6. Rekomendasi mitigasi yang sesuai, misalnya menonaktifkan service yang tidak diperlukan, memperbarui atau mengganti software usang, membatasi akses dengan firewall, dan menghapus service tanpa autentikasi.
7. Kesimpulan singkat tentang keterbatasan scan dan hal yang tidak diuji.

## Kriteria penilaian

- Jaringan VirtualBox benar-benar Host-only dan kedua VM berada di subnet lab yang sama.
- IP target ditemukan dan dibuktikan sebagai Metasploitable2.
- Keempat tahap scan dijalankan dan output disimpan.
- Tabel port/service/versi akurat berdasarkan output.
- Analisis memisahkan bukti, inferensi, dan hal yang belum terverifikasi.
- Rekomendasi mitigasi relevan dan laporan tidak mengklaim dampak yang tidak dibuktikan.
