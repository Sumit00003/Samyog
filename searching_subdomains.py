from rich import print
from pyfiglet import figlet_format
import requests
import os

class SubdomainScanner:
    def __init__(self, base_domain, wordlist_path=None, output_file=None):
        self.base_domain = base_domain
        self.wordlist_path = wordlist_path
        self.output_file = output_file

    def send_request(self, url):
        try:
            return requests.get(f"http://{url}")
        except requests.exceptions.ConnectionError:
            return None
        except requests.exceptions.Timeout:
            print(f"[bold yellow][!] Timeout on {url}")
            return None

    def log_result(self, text):
        if self.output_file:
            with open(self.output_file, "a") as f:
                f.write(text + "\n")

    def scan(self):
        if not os.path.exists(self.wordlist_path):
            print(f"[bold red][-] Wordlist file not found: {self.wordlist_path}")
            return

        print(f"[bold cyan][*] Starting Subdomain Scan on [bold]{self.base_domain}[/bold cyan]")

        with open(self.wordlist_path, "r") as wordlist_file:
            for line in wordlist_file:
                sub = line.strip()
                test_url = f"{sub}.{self.base_domain}"
                #print(f"[*] Testing: {test_url}", end='\n', flush=True)
                response = self.send_request(test_url)
                if response:
                    result = f"[+] Discovered Subdomain --> {test_url} : {response.status_code}"
                    print(f"\n[bold green]{result}")
                    self.log_result(result)

        print(f"\n[yellow][+] Scan complete. Results saved to: {self.output_file or 'N/A'}")


