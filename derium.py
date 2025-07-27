import os
import platform
import urllib.request
import json
from datetime import datetime

R = '\033[91m'  # Merah
B = '\033[94m'  # Biru
RESET = '\033[0m'

def banner():
    print(f"""{B}
╔═════════════════════════════╗
║     {R}DERIUM TOOLS TERMINAL{B}     ║
╚═════════════════════════════╝{RESET}
""")

def cek_security():
    print(f"{B}[•] Mengecek Keamanan Dasar...{RESET}")
    try:
        os.system("whoami")
        print(f"{B}[✓] User Aktif Terdeteksi.{RESET}")
        os.system("ls /data/data/com.termux/")
        print(f"{B}[✓] Akses Termux Valid.{RESET}")
    except:
        print(f"{R}[!] Akses terbatas atau tidak aman.{RESET}")

def cek_internet():
    try:
        urllib.request.urlopen("http://google.com", timeout=3)
        print(f"{B}[✓] Internet Aktif{RESET}")
    except:
        print(f"{R}[!] Tidak Ada Koneksi Internet{RESET}")

def penyimpanan():
    os.system("df -h")

def info_perangkat():
    try:
        model = os.popen("getprop ro.product.model").read().strip()
        version = os.popen("getprop ro.build.version.release").read().strip()
        arch = platform.machine()
        print(f"{B}Model   :{RESET} {model}")
        print(f"{B}Android :{RESET} {version}")
        print(f"{B}CPU Arch:{RESET} {arch}")
    except:
        print(f"{R}Gagal membaca info perangkat{RESET}")

def ip_publik():
    os.system("curl ifconfig.me")

def ping_google():
    os.system("ping -c 4 google.com")

def tanggal_waktu():
    now = datetime.now()
    print(f"{B}Tanggal:{RESET} {now.strftime('%d-%m-%Y')}")
    print(f"{B}Waktu  :{RESET} {now.strftime('%H:%M:%S')}")

def kalkulator():
    try:
        expr = input(f"{B}Masukkan operasi (cth 5+6*2): {RESET}")
        hasil = eval(expr)
        print(f"{R}Hasil: {hasil}{RESET}")
    except:
        print(f"{R}Input tidak valid!{RESET}")

def speedtest():
    os.system("curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python")

def scan_jaringan():
    os.system("nmap -sn 192.168.1.0/24")

def info_kernel():
    os.system("uname -a")

def monitor_cpu():
    os.system("top -n 1")

def uptime():
    os.system("uptime")

def qr_generator():
    teks = input(f"{B}Masukkan teks untuk QR: {RESET}")
    os.system(f"qrencode -t ANSIUTF8 '{teks}'")

def menu():
    while True:
        os.system("clear")
        banner()
        print(f"""{B}
[1]  Cek Keamanan (Security Check)
[2]  Cek Internet
[3]  Cek Penyimpanan
[4]  Info Perangkat
[5]  Cek IP Publik
[6]  Ping Google
[7]  Tanggal & Waktu
[8]  Kalkulator
[9]  Speedtest
[10] Scan Jaringan
[11] Info Kernel
[12] Monitor CPU
[13] Uptime
[14] QR Code Generator
[0]  Keluar{RESET}
""")
        pilihan = input(f"{R}Pilih menu: {RESET}")
        fungsi = {
            "1": cek_security,
            "2": cek_internet,
            "3": penyimpanan,
            "4": info_perangkat,
            "5": ip_publik,
            "6": ping_google,
            "7": tanggal_waktu,
            "8": kalkulator,
            "9": speedtest,
            "10": scan_jaringan,
            "11": info_kernel,
            "12": monitor_cpu,
            "13": uptime,
            "14": qr_generator
        }
        if pilihan == "0":
            print(f"{B}Terima kasih telah menggunakan Derium Tools!{RESET}")
            break
        elif pilihan in fungsi:
            os.system("clear")
            banner()
            fungsi[pilihan]()
        else:
            print(f"{R}Pilihan tidak valid!{RESET}")
        input(f"\n{B}Tekan Enter untuk kembali ke menu...{RESET}")

if __name__ == "__main__":
    os.system("clear")
    menu()
