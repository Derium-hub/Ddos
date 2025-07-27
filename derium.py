#!/usr/bin/env python3

import os
import time
import socket
import subprocess
import platform
import requests
from cryptography.fernet import Fernet
from colorama import Fore, init
init(autoreset=True)

DOWNLOAD_DIR = "/storage/emulated/0/Download/termux"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def banner():
    print(Fore.GREEN + '''
     O
    /|\\     DERIUM TOOLS V1
    / \\   ==================
    ''')

def menu():
    print(Fore.CYAN + "\n=== MENU UTAMA ===")
    print(" 1. Security Check")
    print(" 2. Info Perangkat")
    print(" 3. Cek Koneksi Internet")
    print(" 4. Ping ke Website")
    print(" 5. DNS Lookup")
    print(" 6. Scan Port (nmap)")
    print(" 7. Info Android & CPU")
    print(" 8. Kalkulator")
    print(" 9. Cek IP Publik")
    print("10. Cek IP Lokal")
    print("11. Speed Test")
    print("12. Encrypt File")
    print("13. Decrypt File")
    print("14. Cek Host Sekali Ping")
    print("15. Cari File di Storage")
    print("16. Cek Update Termux")
    print("17. Info Jaringan")
    print("18. [DIHAPUS]")
    print("19. Download Audio YouTube")
    print("20. Keluar")

# === FUNGSI ===

def security_check():
    os.system("whoami && id && uname -a")

def device_info():
    os.system("getprop ro.product.manufacturer")
    os.system("getprop ro.product.model")

def check_connection():
    hasil = os.system("ping -c 1 google.com > /dev/null 2>&1")
    print("Status: ONLINE" if hasil == 0 else "Status: OFFLINE")

def ping_website():
    target = input("Masukkan URL: ")
    os.system(f"ping {target}")

def dns_lookup():
    domain = input("Masukkan domain: ")
    os.system(f"nslookup {domain}")

def scan_ports():
    target = input("Target IP/domain: ")
    os.system(f"nmap {target}")

def android_cpu_info():
    os.system("getprop ro.build.version.release && getprop ro.board.platform")

def kalkulator():
    try:
        ekspresi = input("Masukkan perhitungan: ")
        print("Hasil:", eval(ekspresi))
    except:
        print("Format salah!")

def public_ip():
    try:
        ip = requests.get("https://api.ipify.org").text
        print("IP Publik:", ip)
    except:
        print("Tidak bisa ambil IP publik")

def local_ip():
    print("IP Lokal:", socket.gethostbyname(socket.gethostname()))

def speed_test():
    os.system("curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python -")

def encrypt_file():
    filepath = input("Masukkan path file: ")
    key = Fernet.generate_key()
    cipher = Fernet(key)

    try:
        with open(filepath, 'rb') as f:
            data = f.read()
        encrypted = cipher.encrypt(data)

        out_path = os.path.join(DOWNLOAD_DIR, "encrypted_file.enc")
        with open(out_path, 'wb') as f:
            f.write(encrypted)

        with open(os.path.join(DOWNLOAD_DIR, "enc_key.key"), 'wb') as f:
            f.write(key)

        print("File terenkripsi disimpan:", out_path)
        print("Key disimpan:", os.path.join(DOWNLOAD_DIR, "enc_key.key"))
    except Exception as e:
        print("Gagal:", e)

def decrypt_file():
    filepath = input("Masukkan path file terenkripsi: ")
    key_path = input("Masukkan path key: ")

    try:
        with open(key_path, 'rb') as f:
            key = f.read()
        cipher = Fernet(key)

        with open(filepath, 'rb') as f:
            encrypted_data = f.read()
        decrypted = cipher.decrypt(encrypted_data)

        out_path = os.path.join(DOWNLOAD_DIR, "decrypted_file.txt")
        with open(out_path, 'wb') as f:
            f.write(decrypted)

        print("File berhasil didekripsi:", out_path)
    except Exception as e:
        print("Gagal:", e)

def check_host():
    host = input("Masukkan host: ")
    os.system(f"ping -c 1 {host}")

def cari_file():
    nama = input("Masukkan nama file: ")
    os.system(f"find /sdcard -name \"{nama}\"")

def check_update():
    os.system("pkg update && pkg upgrade -y")

def jaringan_info():
    os.system("ip a")

def download_video():
    url = input("URL YouTube: ")
    os.system(f"yt-dlp -f best -o '{DOWNLOAD_DIR}/%(title)s.%(ext)s' {url}")
    print(f"Video berhasil diunduh ke: {DOWNLOAD_DIR}")

# === MAIN LOOP ===

while True:
    os.system("clear")
    banner()
    menu()
    try:
        pilihan = input("\nPilih nomor menu: ")
        if pilihan == "1":
            security_check()
        elif pilihan == "2":
            device_info()
        elif pilihan == "3":
            check_connection()
        elif pilihan == "4":
            ping_website()
        elif pilihan == "5":
            dns_lookup()
        elif pilihan == "6":
            scan_ports()
        elif pilihan == "7":
            android_cpu_info()
        elif pilihan == "8":
            kalkulator()
        elif pilihan == "9":
            public_ip()
        elif pilihan == "10":
            local_ip()
        elif pilihan == "11":
            speed_test()
        elif pilihan == "12":
            encrypt_file()
        elif pilihan == "13":
            decrypt_file()
        elif pilihan == "14":
            check_host()
        elif pilihan == "15":
            cari_file()
        elif pilihan == "16":
            check_update()
        elif pilihan == "17":
            jaringan_info()
        elif pilihan == "19":
            download_video()
        elif pilihan == "20":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid.")
    except KeyboardInterrupt:
        print("\nDibatalkan oleh pengguna.")
    
    input("\nTekan Enter untuk kembali ke menu...")
