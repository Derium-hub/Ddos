import os
import time

# Warna ANSI
R = '\033[91m'  # Merah
G = '\033[92m'  # Hijau
Y = '\033[93m'  # Kuning
B = '\033[94m'  # Biru
C = '\033[96m'  # Cyan
W = '\033[97m'  # Putih
RESET = '\033[0m'

def banner():
    print(f"""{R}
██████╗ ███████╗██████╗ ██╗██╗   ██╗███╗   ███╗    {B}████████╗ ██████╗  ██████╗ ██╗     ███████╗██╗███████╗
██╔══██╗██╔════╝██╔══██╗██║██║   ██║████╗ ████║    {B}╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝██║██╔════╝
██████╔╝█████╗  ██████╔╝██║██║   ██║██╔████╔██║       ██║   ██║   ██║██║   ██║██║     █████╗  ██║█████╗  
██╔═══╝ ██╔══╝  ██╔═══╝ ██║██║   ██║██║╚██╔╝██║       ██║   ██║   ██║██║   ██║██║     ██╔══╝  ██║██╔══╝  
██║     ███████╗██║     ██║╚██████╔╝██║ ╚═╝ ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████╗██║███████╗
╚═╝     ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝     ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝╚══════╝{RESET}
""")

def menu():
    print(f"""{C}
[1] Port Scanner
[2] DNS Lookup
[3] IP Geolocation
[4] Reverse IP
[5] Admin Finder
[6] Ping Website
[7] Device Info
[8] Exit{RESET}
""")

def dummy_action(name):
    print(f"{C}\n[+] Menjalankan {name}...\n{RESET}")
    time.sleep(1)

def device_info():
    try:
        model = os.popen("getprop ro.product.model").read().strip()
        android_version = os.popen("getprop ro.build.version.release").read().strip()
        ram = os.popen("free -h | grep Mem | awk '{print $2}'").read().strip()
        rom = os.popen("df -h /data | tail -1 | awk '{print $2}'").read().strip()

        print(f"{Y}\n[•] Nama Produk     : {model}")
        print(f"[•] Versi Android   : {android_version}")
        print(f"[•] RAM Tersedia    : {ram}")
        print(f"[•] ROM Tersedia    : {rom}{RESET}")
    except Exception as e:
        print(f"{R}[!] Gagal mendapatkan info perangkat: {e}{RESET}")
    input(f"{B}\nTekan Enter untuk kembali ke menu...{RESET}")

def main():
    while True:
        os.system("clear")
        banner()
        menu()
        pilihan = input(f"{G}Pilih menu > {RESET}")
        if pilihan == '1':
            dummy_action("Port Scanner")
        elif pilihan == '2':
            dummy_action("DNS Lookup")
        elif pilihan == '3':
            dummy_action("IP Geolocation")
        elif pilihan == '4':
            dummy_action("Reverse IP")
        elif pilihan == '5':
            dummy_action("Admin Finder")
        elif pilihan == '6':
            target = input("Masukkan URL/domain: ")
            os.system(f"ping -c 4 {target}")
            input(f"{B}Tekan Enter untuk kembali ke menu...{RESET}")
        elif pilihan == '7':
            device_info()
        elif pilihan == '8':
            print(f"{Y}Terima kasih telah menggunakan DERIUM TOOLS!{RESET}")
            break
        else:
            print(f"{R}Pilihan tidak valid.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
