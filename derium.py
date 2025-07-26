import os, socket, requests, platform, speedtest
from random import choice

# Warna
R = '\033[91m'  # Merah
B = '\033[94m'  # Biru
W = '\033[97m'  # Putih
C = '\033[96m'  # Cyan
RESET = '\033[0m'

# Banner keren
def banner():
    os.system("clear")
    print(f"""{R}
██████╗ ███████╗██████╗ ██╗██╗   ██╗███╗   ███╗
██╔══██╗██╔════╝██╔══██╗██║██║   ██║████╗ ████║
██████╔╝█████╗  ██████╔╝██║██║   ██║██╔████╔██║
██╔═══╝ ██╔══╝  ██╔═══╝ ██║██║   ██║██║╚██╔╝██║
██║     ███████╗██║     ██║╚██████╔╝██║ ╚═╝ ██║
╚═╝     ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝     ╚═╝
        {B}DeriumTools by Derium-hub{RESET}
""")

def menu():
    print(f"{B}1.{W} Ping Website")
    print(f"{B}2.{W} IP Lookup")
    print(f"{B}3.{W} DNS Lookup")
    print(f"{B}4.{W} Port Scanner")
    print(f"{B}5.{W} Speedtest Internet")
    print(f"{B}6.{W} Random User-Agent")
    print(f"{B}7.{W} Random Quote")
    print(f"{B}8.{W} Info Sistem")
    print(f"{B}9.{W} 📱 Info HP Saya")
    print(f"{B}0.{W} Keluar")
    return input(f"\n{C}Pilih menu >> {RESET}")

def ping():
    os.system("ping -c 4 " + input("Masukkan URL/IP: "))

def ip_lookup():
    try:
        host = input("Masukkan domain: ")
        ip = socket.gethostbyname(host)
        print(f"{G}IP Address: {ip}{RESET}")
    except:
        print("Gagal mendapatkan IP.")

def dns_lookup():
    try:
        domain = input("Domain: ")
        print(socket.gethostbyname_ex(domain))
    except:
        print("DNS lookup gagal.")

def port_scanner():
    target = input("IP Target: ")
    ports = [21, 22, 23, 53, 80, 443, 8080]
    for port in ports:
        s = socket.socket(); s.settimeout(1)
        if s.connect_ex((target, port)) == 0:
            print(f"{R}Port {port} terbuka{RESET}")
        s.close()

def speed_test():
    st = speedtest.Speedtest()
    print("Download:", round(st.download()/1e6, 2), "Mbps")
    print("Upload:", round(st.upload()/1e6, 2), "Mbps")

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
        data = requests.get("https://api.quotable.io/random").json()
        print(f'"{data["content"]}" - {data["author"]}')
    except:
        print("Gagal mengambil quote.")

def info_sistem():
    print("Sistem :", platform.system())
    print("Versi  :", platform.version())
    print("Platform:", platform.platform())
    print("CPU    :", platform.machine())

def info_hp():
    print("📱 Info HP Kamu:")
    print("- OS          :", platform.system())
    print("- Kernel      :", platform.release())
    print("- Arsitektur  :", platform.machine())
    print("- Hostname    :", socket.gethostname())
    try:
        ip = socket.gethostbyname(socket.gethostname())
        print("- IP Lokal    :", ip)
    except:
        print("- IP Lokal    : Tidak Terdeteksi")
    if os.path.exists("/data/data/com.termux"):
        print("- Kamu pakai Termux ✅")

while True:
    banner()
    pilihan = menu()
    if pilihan == "1": ping()
    elif pilihan == "2": ip_lookup()
    elif pilihan == "3": dns_lookup()
    elif pilihan == "4": port_scanner()
    elif pilihan == "5": speed_test()
    elif pilihan == "6": user_agent()
    elif pilihan == "7": quote()
    elif pilihan == "8": info_sistem()
    elif pilihan == "9": info_hp()
    elif pilihan == "0":
        print(f"{R}Keluar...{RESET}")
        break
    else:
        print(f"{R}Menu tidak valid!{RESET}")
    input(f"\n{B}Tekan Enter untuk kembali ke menu...{RESET}")
