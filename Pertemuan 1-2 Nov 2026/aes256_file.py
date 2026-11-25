
import argparse
import os
import sys
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

MAGIC = b"AES256GCM1"
NONCE_SIZE = 12  # Ukuran nonce yang direkomendasikan untuk AES-GCM.


def load_key(key_path: Path) -> bytes:
    """Membaca key dan memastikan panjangnya tepat 32 byte (256 bit)."""
    key = key_path.read_bytes()
    if len(key) != 32:
        raise ValueError(
            f"Key tidak valid: harus 32 byte (256 bit), tetapi ditemukan {len(key)} byte."
        )
    return key


def generate_key(key_path: Path, force: bool = False) -> None:
    """Membuat key AES-256 secara acak dan menyimpannya ke file terpisah."""
    if key_path.exists() and not force:
        raise FileExistsError(
            f"{key_path} sudah ada. Gunakan --force jika memang ingin menggantinya."
        )

    key = AESGCM.generate_key(bit_length=256)
    key_path.parent.mkdir(parents=True, exist_ok=True)
    key_path.write_bytes(key)

    # Membatasi akses file key pada sistem POSIX (misalnya Linux/Kali).
    # Pada Windows, atur izin file melalui pengaturan keamanan/ACL Windows.
    try:
        os.chmod(key_path, 0o600)
    except OSError:
        pass

    print(f"[OK] Key AES-256 berhasil dibuat: {key_path}")
    print("[PERINGATAN] Simpan key dengan aman dan jangan membagikannya.")


def encrypt_file(input_path: Path, output_path: Path, key_path: Path) -> None:
    """Mengenkripsi file dan menyimpan nonce + ciphertext ke file .enc."""
    key = load_key(key_path)
    plaintext = input_path.read_bytes()

    # Nonce harus unik untuk setiap enkripsi dengan key yang sama.
    nonce = os.urandom(NONCE_SIZE)
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(MAGIC + nonce + ciphertext)
    print(f"[OK] File berhasil dienkripsi: {output_path}")


def decrypt_file(input_path: Path, output_path: Path, key_path: Path) -> None:
    """Mendekripsi file .enc dan mengembalikan plaintext."""
    key = load_key(key_path)
    encrypted_data = input_path.read_bytes()

    minimum_size = len(MAGIC) + NONCE_SIZE + 16  # Tag autentikasi GCM 16 byte.
    if len(encrypted_data) < minimum_size or not encrypted_data.startswith(MAGIC):
        raise ValueError("Format file .enc tidak valid atau file terlalu pendek.")

    offset = len(MAGIC)
    nonce = encrypted_data[offset:offset + NONCE_SIZE]
    ciphertext = encrypted_data[offset + NONCE_SIZE:]

    # AES-GCM juga memeriksa integritas/authenticity. Jika key salah atau data
    # berubah, proses dekripsi akan gagal dan tidak menghasilkan plaintext valid.
    plaintext = AESGCM(key).decrypt(nonce, ciphertext, None)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(plaintext)
    print(f"[OK] File berhasil didekripsi: {output_path}")


def verify_files(original_path: Path, decrypted_path: Path) -> None:
    """Membandingkan isi kedua file byte demi byte."""
    original = original_path.read_bytes()
    decrypted = decrypted_path.read_bytes()

    if original == decrypted:
        print("[OK] Verifikasi berhasil: hasil dekripsi IDENTIK dengan file asli.")
    else:
        raise ValueError("Verifikasi gagal: hasil dekripsi berbeda dari file asli.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Enkripsi/dekripsi file menggunakan AES-256-GCM."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    key_parser = subparsers.add_parser("generate-key", help="Buat key AES-256.")
    key_parser.add_argument("--key", type=Path, default=Path("secret.key"))
    key_parser.add_argument("--force", action="store_true",
                             help="Timpa key yang sudah ada (file lama tidak dapat dipulihkan).")

    enc_parser = subparsers.add_parser("encrypt", help="Enkripsi file plaintext.")
    enc_parser.add_argument("--input", type=Path, required=True)
    enc_parser.add_argument("--output", type=Path, required=True)
    enc_parser.add_argument("--key", type=Path, default=Path("secret.key"))

    dec_parser = subparsers.add_parser("decrypt", help="Dekripsi file .enc.")
    dec_parser.add_argument("--input", type=Path, required=True)
    dec_parser.add_argument("--output", type=Path, required=True)
    dec_parser.add_argument("--key", type=Path, default=Path("secret.key"))

    verify_parser = subparsers.add_parser("verify", help="Bandingkan file asli dan hasil dekripsi.")
    verify_parser.add_argument("--original", type=Path, required=True)
    verify_parser.add_argument("--decrypted", type=Path, required=True)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "generate-key":
            generate_key(args.key, args.force)
        elif args.command == "encrypt":
            encrypt_file(args.input, args.output, args.key)
        elif args.command == "decrypt":
            decrypt_file(args.input, args.output, args.key)
        elif args.command == "verify":
            verify_files(args.original, args.decrypted)
        return 0
    except (OSError, ValueError) as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
