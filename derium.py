import os
import platform
import socket
import subprocess
import time

R = '\033[91m'  # Merah
B = '\033[94m'  # Biru
W = '\033[97m'  # Putih
RESET = '\033[0m'

def clear():
    os.system('clear')

def banner():
    print(f"""{R}
       O  
      /|\\     {B}DERIUM TOOLS V1{R}
      / \\    -------------
    """)
    print(f"{B}Tools Serbaguna untuk Pengguna Termux\n{RESET}")

def show_menu():
    print(f"{R}╔════════════════════════════════╗")
    print(f"{R}║{B} Pilih Fungsi Derium Tools      {R}║")
    print(f"{R}╚════════════════════════════════╝{RESET}")
    print(f"{B}1.{RESET} Cek Keamanan (Termux Permissions)")
    print(f"{B}2.{RESET} Lihat Info Sistem")
    print(f"{B}3.{RESET} Lihat Info Jaringan Umum")
    print(f"{B}4.{RESET} Scan Port (Nmap)")
    print(f"{B}5.{RESET} Ping ke Domain/IP")
    print(f"{B}6.{RESET} DNS Lookup")
    print(f"{B}7.{RESET} Lihat Versi Android dan ROM")
    print(f"{B}8.{RESET} Kalkulator Sederhana")
    print(f"{B}9.{RESET} Lihat IP Publik")
    print(f"{B}10.{RESET} Cek Waktu Lokal")
    print(f"{B}11.{RESET} Cek Penggunaan CPU")
    print(f"{B}12.{RESET} Cek Kecepatan Download (fast.com)")
    print(f"{B}13.{RESET} Cek Total Package & Storage")
    print(f"{B}14.{RESET} Buat Catatan Harian")
    print(f"{B}15.{RESET} Ping 1x ke Host")
    print(f"{B}16.{RESET} Cari File di Termux")
    print(f"{B}17.{RESET} Proses CPU Terbesar")
    print(f"{B}18.{RESET} Cek Update Package")
    print(f"{B}19.{RESET} Info Jaringan (Lokal & Interface)")
    print(f"{B}20.{RESET} Info SIM Card (Jika Ada)")
    print(f"{B}21.{RESET} Download YouTube (audio/video)")
    print(f"{B}22.{RESET} Encrypt File Kuat")
    print(f"{B}23.{RESET} Decrypt File Kuat")
    print(f"{B}0.{RESET} Keluar")

# Fungsi-fungsi:

def cek_security():
    os.system("termux-setup-storage")
    print(f"{R}Izin storage sudah diminta. Cek juga manual di pengaturan.{RESET}")

def info_sistem():
    print(f"{R}Versi Android: {RESET}" + os.popen("getprop ro.build.version.release").read())
    print(f"{R}ROM: {RESET}" + os.popen("getprop ro.product.manufacturer").read().strip() + " " + os.popen("getprop ro.product.model").read().strip())

def info_jaringan_umum():
    os.system("ifconfig")

def scan_port():
    target = input(f"{B}Masukkan IP/domain: {RESET}")
    os.system(f"nmap {target}")

def ping():
    host = input(f"{B}Masukkan IP/Domain: {RESET}")
    os.system(f"ping -c 4 {host}")

def dns_lookup():
    domain = input(f"{B}Masukkan domain: {RESET}")
    os.system(f"nslookup {domain}")

def versi_android_rom():
    os.system("getprop ro.build.version.release")
    os.system("getprop ro.product.model")

def kalkulator():
    try:
        expr = input(f"{B}Masukkan operasi (contoh: 5+2*3): {RESET}")
        result = eval(expr)
        print(f"{R}Hasil: {result}{RESET}")
    except Exception as e:
        print(f"{R}Error: {e}{RESET}")

def ip_publik():
    os.system("curl ifconfig.me")

def waktu_lokal():
    os.system("date")

def cek_cpu():
    os.system("top -n 1 | head -n 10")

def speedtest():
    os.system("fast")

def total_pkg_storage():
    os.system("df -h")
    os.system("pkg list-installed | wc -l")

def catatan_harian():
    note = input(f"{B}Tulis catatan: {RESET}")
    with open("notes.txt", "a") as f:
        f.write(f"- {note}\n")
    print(f"{R}Catatan disimpan di notes.txt{RESET}")

def ping1x():
    host = input(f"{B}Masukkan domain/IP: {RESET}")
    os.system(f"ping -c 1 {host}")

def cari_file():
    nama = input(f"{B}Nama file yang dicari: {RESET}")
    os.system(f"find . -name '*{nama}*'")

def proses_cpu_besar():
    os.system("ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head")

def cek_update():
    os.system("pkg update")

def info_jaringan():
    os.system("ip addr show")

def info_sim():
    os.system("termux-telephony-deviceinfo")

def download_youtube():
    url = input(f"{B}Masukkan URL YouTube: {RESET}")
    tipe = input(f"{B}Audio atau Video (a/v): {RESET}").lower()
    if tipe == "a":
        os.system(f"yt-dlp -x --audio-format mp3 {url}")
    else:
        os.system(f"yt-dlp {url}")

def encrypt_file():
    file = input(f"{B}Path file yang akan dienkripsi: {RESET}")
    key = input(f"{B}Masukkan password: {RESET}")
    output = "/data/data/com.termux/files/home/storage/downloads/encrypted_file.enc"
    os.system(f"openssl enc -aes-256-cbc -salt -in '{file}' -out '{output}' -k '{key}'")
    print(f"{R}File terenkripsi disimpan di: {output}{RESET}")

def decrypt_file():
    file = input(f"{B}Path file terenkripsi: {RESET}")
    key = input(f"{B}Masukkan password: {RESET}")
    output = "/data/data/com.termux/files/home/storage/downloads/decrypted_file.txt"
    os.system(f"openssl enc -aes-256-cbc -d -in '{file}' -out '{output}' -k '{key}'")
    print(f"{R}File didekripsi disimpan di: {output}{RESET}")

# Main
while True:
    clear()
    banner()
    show_menu()
    try:
        choice = int(input(f"\n{B}Pilih menu (0-23): {RESET}"))
        if choice == 0:
            print(f"{R}Keluar...{RESET}")
            break
        elif choice == 1: cek_security()
        elif choice == 2: info_sistem()
        elif choice == 3: info_jaringan_umum()
        elif choice == 4: scan_port()
        elif choice == 5: ping()
        elif choice == 6: dns_lookup()
        elif choice == 7: versi_android_rom()
        elif choice == 8: kalkulator()
        elif choice == 9: ip_publik()
        elif choice == 10: waktu_lokal()
        elif choice == 11: cek_cpu()
        elif choice == 12: speedtest()
        elif choice == 13: total_pkg_storage()
        elif choice == 14: catatan_harian()
        elif choice == 15: ping1x()
        elif choice == 16: cari_file()
        elif choice == 17: proses_cpu_besar()
        elif choice == 18: cek_update()
        elif choice == 19: info_jaringan()
        elif choice == 20: info_sim()
        elif choice == 21: download_youtube()
        elif choice == 22: encrypt_file()
        elif choice == 23: decrypt_file()
        else:
            print(f"{R}Menu tidak ditemukan.{RESET}")
    except ValueError:
        print(f"{R}Input tidak valid!{RESET}")
    input(f"\n{B}Tekan Enter untuk kembali ke menu...{RESET}")
