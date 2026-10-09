import argparse
import csv
import re
from collections import Counter
from pathlib import Path

# Pola Regex untuk tanggal dan alamat IPv4 pada auth.log.
DATE_PATTERN = re.compile(r"^([A-Z][a-z]{2}\s+\d{1,2})\s")
IP_PATTERN = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
FAILED_PATTERN = re.compile(r"Failed password.*?from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
ACCEPTED_PATTERN = re.compile(r"Accepted password.*?from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")


def normalize_date(value):
    """Normalisasi tanggal log, misalnya 'Mar  5' menjadi 'Mar 5'."""
    parts = value.strip().split()
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("Format tanggal harus seperti 'Mar 15'.")
    month, day = parts
    if not re.fullmatch(r"[A-Z][a-z]{2}", month) or not day.isdigit() or not 1 <= int(day) <= 31:
        raise argparse.ArgumentTypeError("Format tanggal harus seperti 'Mar 15'.")
    return f"{month} {int(day)}"


def analyze_log(input_path, output_path, threshold=5, selected_date=None):
    failed_counts = Counter()
    accepted_counts = Counter()
    total_lines = 0
    matched_lines = 0

    try:
        with open(input_path, "r", encoding="utf-8", errors="replace") as log_file:
            for line in log_file:
                total_lines += 1
                date_match = DATE_PATTERN.search(line)
                line_date = normalize_date(date_match.group(1)) if date_match else None

                if selected_date is not None and line_date != selected_date:
                    continue

                matched_lines += 1
                failed_match = FAILED_PATTERN.search(line)
                if failed_match:
                    failed_counts[failed_match.group(1)] += 1

                accepted_match = ACCEPTED_PATTERN.search(line)
                if accepted_match:
                    accepted_counts[accepted_match.group(1)] += 1

    except FileNotFoundError:
        raise SystemExit(f"Error: file '{input_path}' tidak ditemukan.")
    except PermissionError:
        raise SystemExit(f"Error: tidak memiliki izin untuk membaca '{input_path}'.")

    suspects = [(ip, count) for ip, count in failed_counts.items() if count > threshold]
    normal = [(ip, count) for ip, count in failed_counts.items() if count <= threshold]

    try:
        with open(output_path, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["IP Address", "Failed Attempts", "Status"])
            for ip, count in sorted(failed_counts.items(), key=lambda item: (-item[1], item[0])):
                status = "SUSPECT" if count > threshold else "NORMAL"
                writer.writerow([ip, count, status])
    except PermissionError:
        raise SystemExit(f"Error: tidak memiliki izin untuk menulis '{output_path}'.")

    print("=== STATISTIK LOG ANALYZER ===")
    print(f"File log                 : {input_path}")
    print(f"Filter tanggal           : {selected_date or 'Semua tanggal'}")
    print(f"Jumlah baris dalam file  : {total_lines}")
    print(f"Baris yang dianalisis    : {matched_lines}")
    print(f"Total failed login      : {sum(failed_counts.values())}")
    print(f"IP dengan failed login  : {len(failed_counts)}")
    print(f"IP berstatus SUSPECT    : {len(suspects)} (lebih dari {threshold} percobaan gagal)")
    print(f"IP berstatus NORMAL     : {len(normal)} (maksimal {threshold} percobaan gagal)")
    print(f"Total Accepted password : {sum(accepted_counts.values())}")
    print(f"IP dengan login berhasil: {len(accepted_counts)}")
    print(f"Laporan CSV             : {output_path}")

    if accepted_counts:
        print("\nAccepted password per IP:")
        for ip, count in sorted(accepted_counts.items(), key=lambda item: (-item[1], item[0])):
            print(f"  {ip}: {count}")
    else:
        print("\nTidak ada event 'Accepted password' pada tanggal/filter tersebut.")

    print("\nStatus IP berdasarkan failed login:")
    if failed_counts:
        for ip, count in sorted(failed_counts.items(), key=lambda item: (-item[1], item[0])):
            status = "SUSPECT" if count > threshold else "NORMAL"
            print(f"  {ip}: {count} percobaan — {status}")
    else:
        print("  Tidak ada failed login yang ditemukan.")


def main():
    parser = argparse.ArgumentParser(
        description="Analisis auth.log untuk menghitung failed login dan mendeteksi IP suspect."
    )
    parser.add_argument("-i", "--input", default="auth.log", help="Path file log (default: auth.log)")
    parser.add_argument("-o", "--output", default="report.csv", help="Path laporan CSV (default: report.csv)")
    parser.add_argument("-t", "--threshold", type=int, default=5, help="Ambang failed login; suspect jika lebih dari nilai ini (default: 5)")
    parser.add_argument("-d", "--date", type=normalize_date, help="Filter tanggal, contoh: 'Mar 15' (opsional)")
    args = parser.parse_args()

    if args.threshold < 0:
        parser.error("threshold tidak boleh negatif")

    analyze_log(args.input, args.output, args.threshold, args.date)


if __name__ == "__main__":
    main()
