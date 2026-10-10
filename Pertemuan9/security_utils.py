import random
import string
import re


def generate_random_password(length=16):
    """
    Membuat password acak dengan kombinasi huruf,
    angka, dan simbol.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def is_valid_ip(ip):
    """
    Mengecek apakah format alamat IPv4 valid menggunakan regex.
    Mengembalikan True atau False.
    """
    pattern = r'^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$'

    if re.match(pattern, ip):
        return True
    return False


def bytes_to_human(bytes_value):
    """
    Mengubah ukuran bytes menjadi KB, MB, atau GB.
    """
    if bytes_value < 1024:
        return f"{bytes_value} Bytes"
    elif bytes_value < 1024 ** 2:
        return f"{bytes_value / 1024:.2f} KB"
    elif bytes_value < 1024 ** 3:
        return f"{bytes_value / (1024 ** 2):.2f} MB"
    else:
        return f"{bytes_value / (1024 ** 3):.2f} GB"