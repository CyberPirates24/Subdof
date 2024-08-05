import requests
import sys
import os

def clear_screen():
    # Clear the terminal screen
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-like systems (Linux, macOS, etc.)
        os.system('clear')

def print_banner():
    print("\033[92m")
    print('███████╗██╗   ██╗██████╗ ██████╗  ██████╗ ███████╗')
    print('██╔════╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗██╔════╝')
    print('███████╗██║   ██║██████╔╝██║  ██║██║   ██║█████╗  ')
    print('╚════██║██║   ██║██╔══██╗██║  ██║██║   ██║██╔══╝  ')
    print('███████║╚██████╔╝██████╔╝██████╔╝╚██████╔╝██║     ')
    print('╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═╝     ')

def get_subdomains_virustotal(domain):
    print("\033[93m")
    print("[*] Enumerating subdomains using VirusTotal...")
    api_url = f"https://www.virustotal.com/vtapi/v2/domain/report?apikey=cc825abe48e33fd25a382fb508ab2dbc01d4eb7f369ca0cfba178d61877d119e&domain={domain}"
    response = requests.get(api_url)
    subdomains = set()
    
    if response.status_code == 200:
        data = response.json()
        if 'subdomains' in data:
            subdomains.update(data['subdomains'])
    
    return subdomains

def get_subdomains_crtsh(domain):
    print("\033[93m")
    print("[*] Enumerating subdomains using crt.sh...")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    response = requests.get(url)
    subdomains = set()

    if response.status_code == 200:
        data = response.json()
        for entry in data:
            subdomains.update(entry['name_value'].split('\n'))
    
    return subdomains

def get_subdomains_hackertarget(domain):
    print("\033[93m")
    print("[*] Enumerating subdomains using HackerTarget...")
    url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
    response = requests.get(url)
    subdomains = set()

    if response.status_code == 200:
        data = response.text
        for line in data.splitlines():
            parts = line.split(',')
            if len(parts) > 1 and parts[0].endswith(domain):
                subdomains.add(parts[0])
    
    return subdomains

def combine_results(results):
    print("\033[92m")
    all_subdomains = set()
    for result in results:
        all_subdomains.update(result)
    return all_subdomains

def save_results(subdomains):
    filename = input("Enter the filename to save results (e.g., results.txt): ").strip()
    if not filename:
        print("Error: No filename entered. Results not saved.")
        return
    
    with open(filename, 'w') as file:
        for subdomain in sorted(subdomains):
            file.write(f"{subdomain}\n")

    print(f"[*] Results saved to {filename}")

def main(domain):
    subdomains_virustotal = get_subdomains_virustotal(domain)
    subdomains_crtsh = get_subdomains_crtsh(domain)
    subdomains_hackertarget = get_subdomains_hackertarget(domain)

    all_subdomains = combine_results([subdomains_virustotal, subdomains_crtsh, subdomains_hackertarget])

    print("[*] Subdomain enumeration completed.")
    for subdomain in sorted(all_subdomains):
        print(subdomain)

    save_results(all_subdomains)

if __name__ == "__main__":
    clear_screen()
    print_banner()
    domain = input("Enter Your Domain: ").strip()
    if not domain:
        print("Error: No domain entered.")
        sys.exit(1)
    
    main(domain)
