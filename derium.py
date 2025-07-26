import os
import time
import platform
import urllib.request
from datetime import datetime
import subprocess

R = '\033[91m'  # Merah
B = '\033[94m'  # Biru
RESET = '\033[0m'

def banner():
    print(f"""{R}
██████╗ ███████╗██████╗ ██╗██╗   ██╗███╗   ███╗    {B}████████╗ ██████╗  ██████╗ ██╗     ██╗███████╗
██╔══██╗██╔════╝██╔══██╗██║██║   ██║████╗ ████║    {R}╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██║██╔════╝
██████╔╝█████╗  ██████╔╝██║██║   ██║██╔████╔██║       ██║   ██║   ██║██║   ██║██║     ██║███████╗
██╔═══╝ ██╔══╝  ██╔═══╝ ██║██║   ██║██║╚██╔╝██║       ██║   ██║   ██║██║   ██║██║     ██║╚════██║
██║     ███████╗██║     ██║╚██████╔╝██║ ╚═╝ ██║       ██║   ╚██████╔╝╚██████╔╝███████╗██║███████║
╚═╝     ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝     ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚══════╝
{RESET}""")

# Fungsi berguna
def cek_internet():
    try:
        urllib.request.urlopen("http://google.com", timeout=3)
        print(f"{B}[✓] Internet Aktif{RESET}")
    except:
        print(f"{R}[!] Tidak Ada Koneksi Internet{RESET}")

def baterai():
    os.system("termux-battery-status")

def penyimpanan():
    os.system("df -h")

def info():
    os.system("termux-info")

def ip_pub():
    os.system("curl ifconfig.me")

def ping():
    os.system("ping -c 4 google.com")

def waktu():
    now = datetime.now()
    print(f"{B}Tanggal:{RESET} {now.strftime('%d-%m-%Y')}")
    print(f"{B}Waktu  :{RESET} {now.strftime('%H:%M:%S')}")

def kalkulator():
    try:
        expr = input(f"{B}Operasi (cth 5+6*2): {RESET}")
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

def daftar_aplikasi():
    os.system("pm list packages")

def clipboard():
    os.system("termux-clipboard-get")

def cpu_monitor():
    os.system("top -n 1")

def uptime():
    os.system("uptime")

def flashlight_on():
    os.system("termux-torch on")

def flashlight_off():
    os.system("termux-torch off")

def lokasi():
    os.system("termux-location")

def sensor():
    os.system("termux-sensor -n accelerometer,gyroscope")

def qr_generator():
    teks = input(f"{B}Masukkan teks QR: {RESET}")
    os.system(f"qrencode -t ANSIUTF8 '{teks}'")

# Menu
def menu():
    while True:
        print(f"""{B}
[1] Cek Internet     [2] Status Baterai    [3] Cek Penyimpanan
[4] Info Perangkat   [5] Cek IP Publik     [6] Ping Google
[7] Tanggal & Waktu  [8] Kalkulator        [9] Speedtest
[10] Scan Jaringan   [11] Info Kernel      [12] Daftar Aplikasi
[13] Clipboard Isi   [14] Monitor CPU      [15] Waktu Aktif
[16] Flashlight ON   [17] Flashlight OFF   [18] Lokasi Sekarang
[19] Sensor Deteksi  [20] QR Code Generator
[0] Keluar
{RESET}""")
        pilihan = input(f"{R}Pilih menu: {RESET}")
        if pilihan == "1": cek_internet()
        elif pilihan == "2": baterai()
        elif pilihan == "3": penyimpanan()
        elif pilihan == "4": info()
        elif pilihan == "5": ip_pub()
        elif pilihan == "6": ping()
        elif pilihan == "7": waktu()
        elif pilihan == "8": kalkulator()
        elif pilihan == "9": speedtest()
        elif pilihan == "10": scan_jaringan()
        elif pilihan == "11": info_kernel()
        elif pilihan == "12": daftar_aplikasi()
        elif pilihan == "13": clipboard()
        elif pilihan == "14": cpu_monitor()
        elif pilihan == "15": uptime()
        elif pilihan == "16": flashlight_on()
        elif pilihan == "17": flashlight_off()
        elif pilihan == "18": lokasi()
        elif pilihan == "19": sensor()
        elif pilihan == "20": qr_generator()
        elif pilihan == "0":
            print(f"{R}Keluar...{RESET}")
            break
        else:
            print(f"{R}Pilihan tidak valid!{RESET}")
        input(f"{B}Tekan Enter untuk kembali...{RESET}")
        os.system("clear")
        banner()

if __name__ == "__main__":
    os.system("clear")
    banner()
    menu()
