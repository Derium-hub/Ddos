import os
import socket
import requests
import platform
import speedtest
from random import choice

# Warna ANSI
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
C = '\033[96m'
W = '\033[0m'

banner = f"""{C}
   ____           _                 
  |  _ \ ___  ___| |_ _ __ ___  ___ 
  | | | / _ \/ __| __| '__/ _ \/ _ \\
  | |_| |  __/\__ \ |_| | |  __/  __/
  |____/ \___||___/\__|_|  \___|\___|

   - DeriumTools by Derium-hub -
{W}"""

def menu():
    print(banner)
    print(f"{Y}1.{W} Ping Website")
    print(f"{Y}2.{W} IP Lookup")
    print(f"{Y}3.{W} DNS Lookup")
    print(f"{Y}4.{W} Port Scanner")
    print(f"{Y}5.{W} Speedtest Internet")
    print(f"{Y}6.{W} Random User-Agent")
    print(f"{Y}7.{W} Random Quote")
    print(f"{Y}8.{W} System Info")
    print(f"{Y}0.{W} Keluar")
    return input(f"{C}\nPilih menu >> {W}")

def ping():
    target = input("Masukkan URL/IP: ")
    os.system(f"ping -c 4 {target}")

def ip_lookup():
    host = input("Masukkan domain: ")
    try:
        ip = socket.gethostbyname(host)
        print(f"{G}IP Address: {ip}{W}")
    except:
        print(f"{R}Gagal mendapatkan IP.{W}")

def dns_lookup():
    domain = input("Masukkan domain: ")
    try:
        info = socket.gethostbyname_ex(domain)
        print(f"{G}DNS Result: {info}{W}")
    except:
        print(f"{R}Gagal lookup DNS.{W}")

def port_scanner():
    target = input("IP Target: ")
    ports = [21, 22, 23, 53, 80, 443, 8080]
    print(f"{C}Scanning...{W}")
    for port in ports:
        s = socket.socket()
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"{G}Port {port} terbuka{W}")
        s.close()

def speed_test():
    print(f"{C}Sedang mengetes kecepatan...{W}")
    st = speedtest.Speedtest()
    down = st.download() / 1_000_000
    up = st.upload() / 1_000_000
    print(f"Download: {down:.2f} Mbps")
    print(f"Upload  : {up:.2f} Mbps")

def user_agent():
    agents = [
        "Mozilla/5.0 (Linux; Android 10)",
        "Mozilla/5.0 (Windows NT 10.0)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
    ]
    print("User-Agent:", choice(agents))

def quote():
    try:
        r = requests.get("https://api.quotable.io/random")
        data = r.json()
        print(f'"{data["content"]}" - {data["author"]}')
    except:
        print("Gagal mengambil quote.")

def sys_info():
    print("Sistem :", platform.system())
    print("Versi  :", platform.version())
    print("Mesin  :", platform.machine())

def main():
    while True:
        pilih = menu()
        if pilih == "1": ping()
        elif pilih == "2": ip_lookup()
        elif pilih == "3": dns_lookup()
        elif pilih == "4": port_scanner()
        elif pilih == "5": speed_test()
        elif pilih == "6": user_agent()
        elif pilih == "7": quote()
        elif pilih == "8": sys_info()
        elif pilih == "0":
            print("Keluar...")
            break
        else:
            print(f"{R}Pilihan tidak valid!{W}")
        input(f"\n{C}Tekan Enter untuk kembali ke menu...{W}")

if __name__ == "__main__":
    main()
