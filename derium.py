import os
import socket
import requests
import platform

# Warna
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
C = '\033[96m'
W = '\033[97m'
RESET = '\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(f"""{B}
┌───────────────────────────────────────────────┐
│  {R}DERIUM HackSuite{B}  -  {C}v1.0{B}                         │
├───────────────────────────────────────────────┤
│  {W}Author :{C} Derium-hub                                {B}│
│  {W}Status :{C} Online                                     {B}│
│  {W}Tools  :{C} Scanner | Lookup | Ping                   {B}│
└───────────────────────────────────────────────┘{RESET}
""")

def menu():
    print(f"""{G}
[1]  Port Scanner
[2]  DNS Lookup
[3]  IP Geolocation
[4]  HTTP Header Check
[5]  Reverse IP Lookup
[6]  Ping Website
[7]  Device Info
[8]  Exit Tool{RESET}
""")
    return input(f"{C}Pilih menu > {RESET}")

def port_scanner():
    host = input(f"{Y}Masukkan host target: {RESET}")
    ports = [21, 22, 23, 80, 443, 8080]
    print(f"{C}Memindai port...{RESET}")
    for port in ports:
        s = socket.socket()
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"{G}[OPEN] Port {port}{RESET}")
        s.close()

def dns_lookup():
    domain = input(f"{Y}Masukkan domain: {RESET}")
    try:
        ip = socket.gethostbyname(domain)
        print(f"{C}IP Address: {G}{ip}{RESET}")
    except:
        print(f"{R}Gagal mendapatkan IP{RESET}")

def ip_geolocation():
    ip = input(f"{Y}Masukkan IP: {RESET}")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}").json()
        for k, v in r.items():
            print(f"{W}{k.capitalize():<15}: {C}{v}{RESET}")
    except:
        print(f"{R}Gagal mengambil data lokasi!{RESET}")

def http_header():
    url = input(f"{Y}Masukkan URL (contoh: https://example.com): {RESET}")
    try:
        r = requests.head(url)
        for k, v in r.headers.items():
            print(f"{C}{k}: {G}{v}{RESET}")
    except:
        print(f"{R}Gagal mengambil header!{RESET}")

def reverse_ip():
    ip = input(f"{Y}Masukkan IP: {RESET}")
    try:
        r = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={ip}")
        print(f"{C}{r.text}{RESET}")
    except:
        print(f"{R}Gagal reverse lookup!{RESET}")

def ping_website():
    host = input(f"{Y}Masukkan host: {RESET}")
    os.system(f"ping -c 4 {host}")

def device_info():
    print(f"\n{G}[+] Menjalankan Device Info...{RESET}\n")
    try:
        os_version = platform.release()
        device_name = os.popen("getprop ro.product.model").read().strip()
        processor = platform.processor()

        print(f"{C}Versi OS       : {G}{os_version}{RESET}")
        print(f"{C}Nama Produk    : {G}{device_name}{RESET}")
        print(f"{C}Processor      : {G}{processor}{RESET}")
    except Exception as e:
        print(f"{R}[!] Gagal: {e}{RESET}")
    input(f"{B}\nTekan Enter untuk kembali ke menu...{RESET}")

# Main Program
while True:
    clear()
    banner()
    pilihan = menu()

    if pilihan == '1':
        port_scanner()
    elif pilihan == '2':
        dns_lookup()
    elif pilihan == '3':
        ip_geolocation()
    elif pilihan == '4':
        http_header()
    elif pilihan == '5':
        reverse_ip()
    elif pilihan == '6':
        ping_website()
    elif pilihan == '7':
        device_info()
    elif pilihan == '8':
        print(f"{Y}Keluar...{RESET}")
        break
    else:
        print(f"{R}Pilihan tidak valid!{RESET}")

    input(f"{B}\nTekan Enter untuk kembali ke menu...{RESET}")
