import os
import time

# Warna ANSI
R = "\033[91m"   # Merah
B = "\033[94m"   # Biru
C = "\033[96m"   # Cyan
RESET = "\033[0m"

# Banner
def banner():
    os.system("clear")
    print(f"""{B}
╔════════════════════════════════════════════╗
║         {R}DERIUM HackSuite{B}  -  v1.0             ║
╠════════════════════════════════════════════╣
║  Author  : Derium-hub                      ║
║  Status  : Online                          ║
║  Tools   : Scanner | Lookup | Ping         ║
╚════════════════════════════════════════════╝{RESET}
""")

# Menu
def show_menu():
    print(f"""{C}
[1]  Port Scanner
[2]  DNS Lookup
[3]  IP Geolocation
[4]  HTTP Header Check
[5]  Reverse IP Lookup
[6]  Ping Website
[7]  Device Info
[8]  Exit Tool
{RESET}""")

# Fungsi dummy (sementara)
def dummy_action(name):
    print(f"{C}\n[+] Menjalankan {name}...\n{RESET}")
    time.sleep(1)

# Main program
def main():
    banner()
    while True:
        show_menu()
        try:
            pilihan = input(f"{B}Pilih menu > {RESET}")
            if pilihan == '1':
                dummy_action("Port Scanner")
            elif pilihan == '2':
                dummy_action("DNS Lookup")
            elif pilihan == '3':
                dummy_action("IP Geolocation")
            elif pilihan == '4':
                dummy_action("HTTP Header Check")
            elif pilihan == '5':
                dummy_action("Reverse IP Lookup")
            elif pilihan == '6':
                dummy_action("Ping Website")
            elif pilihan == '7':
                dummy_action("Device Info")
            elif pilihan == '8':
                print(f"{R}\n[!] Keluar...{RESET}")
                break
            else:
                print(f"{R}[!] Pilihan tidak valid!{RESET}")
        except KeyboardInterrupt:
            print(f"\n{R}[!] Dihentikan oleh user.{RESET}")
            break

if __name__ == "__main__":
    main()
