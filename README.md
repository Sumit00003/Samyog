💻 SAMYOGA - EH Toolkit

SAMYOGA is a command-line terminal that provides a unified interface for various penetration testing utilities such as keylogger creation, hidden directory discovery, subdomain enumeration, and a basic web crawler.

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

Python 3.x, Wine (for compiling Windows binaries on Linux), PyInstaller (installed via Wine)

Modules: pyfiglet, rich, keylogger  
Install dependencies:

```
pip install pyfiglet rich
```

🛠 Installation

Clone the repository:
```
git clone https://github.com/yourusername/SAMYOGA.git
```
```
cd SAMYOGA
```

✅ Usage Instructions

Make the script executable:  
```
chmod +x install.sh
```

Run the installation:  
```
./install.sh
```

Run the tool using:
```
python samyoga.py
```

You will see an ASCII welcome screen and available commands like:

Available Commands:  
 use : Use a specific tool  
 info : Information on a specific tool  
 exit : Completely exit Tool  

🧪 Tool Details

🔑 1. Keylogger Generator (Windows Only)
Usage:  
use 1  
And Provide the input details carefully.

⚠️ Don't upload keyloggers to VirusTotal as it exposes signatures to antivirus vendors.

📁 2. Hidden Directory Finder  
Usage: use 2

🌐 3. Subdomain Finder  
Usage: use 3

🕷 4. Simple Web Crawler  
Usage: use 4


🔍 Wordlist Defaults

You should edit the paths of the downloaded wordlists in Default_paths.py:

DEFAULT_WORDLIST_DIR = "/your/path/to/directory-list.txt"

DEFAULT_WORDLIST_SUB = "/your/path/to/subdomains.txt"


⚠️ Legal Disclaimer

This tool is intended for educational use only. Usage without permission is strictly prohibited and illegal. The authors are not responsible for any misuse.

🙋‍♂️ Author
Your Name — @Sumit00003
