from rich import print
import requests
from pyfiglet import figlet_format
import os
#from CLI import TARGET_URL, USE_CUSTOM_WORDLIST, CUSTOM_WORDLIST_PATH

class DirectoryScanner:
    #DEFAULT_WORDLIST = "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"

    def __init__(self, target_url, wordlist_path=None,output_file=None):
        self.target_url = target_url
        self.wordlist_path = wordlist_path
        self.output_file = output_file

    def send_request(self, url):
        try:
            return requests.get(url)
        except requests.exceptions.ConnectionError:
            return None
            
    def log_result(self, text):
        if self.output_file:
            with open(self.output_file, "a") as f:
                f.write(text + "\n")
    # def check_slash(self,url, word):
    # 	if url.endswith('/'):
    #         test_url = f"{url}{word}"
    #     else:
    #         test_url = f"{url}/{word}"
    #     return test_url
    

    def scan(self):
        if not os.path.exists(self.wordlist_path):
            print(f"[bold red][-] Wordlist file not found: {self.wordlist_path}")
            return

        with open(self.wordlist_path, "r") as wordlist_file:
            for line in wordlist_file:
                word = line.strip()
                if self.target_url.endswith('/'):
                    test_url = f"{self.target_url}{word}"
                else:
                    test_url = f"{self.target_url}/{word}"    
                print(test_url, end='\r', flush=True)
                response = self.send_request(test_url)
                if response:
                    result = f"[+] Discovered Directory --> {test_url} : {response.status_code}"
                    print(f"[bold green]{result}\n")
                    self.log_result(result)
            print(f"[yellow][+]The Result is Saved in ---> {self.output_file}",end='\n')

'''if __name__ == "__main__":
    try:
        print(figlet_format("Hidden Directories", font="standard"))
        wordlist_path = CUSTOM_WORDLIST_PATH if USE_CUSTOM_WORDLIST else None
        scanner = DirectoryScanner(TARGET_URL, wordlist_path)
        scanner.scan()
    except KeyboardInterrupt:
        print("\n[bold red][-] User has pressed Ctrl + C. Stopping.....")'''

