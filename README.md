💻 SAMYOGA - Offensive Security Toolkit

SAMYOGA is a terminal-based offensive security toolkit that provides a unified interface for various penetration testing utilities such as keylogger creation, hidden directory discovery, subdomain enumeration, and a basic web crawler.

⚠️ Disclaimer: This tool is for educational and ethical hacking purposes only. Unauthorized usage against systems without explicit permission is illegal.

📋 Features
Tool	Description
1	Windows Keylogger Generator: Generates a simple Python keylogger and compiles it into a Windows executable.
2	Hidden Directory Finder: Scans for hidden directories using default or custom wordlists.
3	Subdomain Finder: Searches for subdomains using a default or custom wordlist.
4	Web Crawler (Spider): Crawls a target URL and lists discovered internal links.

🚀 Getting Started
✅ Prerequisites
Ensure the following dependencies and requirements are met:

Python 3.x

Wine (for compiling Windows binaries on Linux)

PyInstaller (installed via Wine or natively on Windows)

Modules:

pyfiglet

rich

keylogger (custom, assumed to be in the project)

Custom modules: Hidden_directorys, searching_subdomains, logo, Spider

Wordlists (custom or default paths in the tool)

Install dependencies:

pip install pyfiglet rich

🛠 Installation
Clone the repository:

git clone https://github.com/yourusername/SAMYOGA.git
cd SAMYOGA

⚙️ Usage
Run the tool using:
python samyoga.py

You will see an ASCII welcome screen and available commands like:
Available Commands:
 use : Use a specific tool
 info : Information on a specific tool
 exit : Completely exit Tool

🧪 Tool Details
🔑 1. Keylogger Generator (Windows Only)
Usage:
use 1
Prompts for:
Email
App-specific password
Time interval
Output file name (will be compiled to .exe)

⚠️ Don't upload keyloggers to VirusTotal as it exposes signatures to antivirus vendors.

📁 2. Hidden Directory Finder
Usage:
use 2
Prompts for:
Target URL (must include http:// or https://)
Option to use custom wordlist
Output filename

🌐 3. Subdomain Finder
Usage:
use 3
Prompts for:
Domain (without http://)
Option to use custom wordlist
Output filename

🕷 4. Simple Web Crawler
Usage:
use 4
Prompts for:
Target URL
Output file to save the crawled links

🔍 Wordlist Defaults
You can edit the paths in Default_paths.py:
DEFAULT_WORDLIST_DIR = "/your/path/to/directory-list.txt"
DEFAULT_WORDLIST_SUB = "/your/path/to/subdomains.txt"

🧰 Modules Structure
graphql
Copy
Edit
SAMYOGA/
│
├── samyoga.py                # Main file
├── keylogger.py              # Custom keylogger logic
├── Hidden_directorys.py      # Hidden directory scanner logic
├── searching_subdomains.py   # Subdomain scanner logic
├── Spider.py                 # Web crawler
├── logo.py                   # ASCII art for exit
├── Default_paths.py          # Default wordlists

⚠️ Legal Disclaimer
This tool is intended for educational use only. Usage without permission is strictly prohibited and illegal. The authors are not responsible for any misuse.

🙋‍♂️ Author
Your Name — @Sumit00003
