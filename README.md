 SAMYOGA - EH Toolkit

SAMYOGA is a command-line terminal that provides a interface for various penetration testing utilities such as keylogger creation, hidden directory discovery, subdomain enumeration, and a basic web crawler.

 Disclaimer: This tool is for educational and ethical hacking purposes only. Unauthorized usage against systems without explicit permission is illegal.

Features  

Tool	Description  
1	Windows Keylogger Generator: Generates a simple Python keylogger and compiles it into a Windows executable.  
2	Hidden Directory Finder: Scans for hidden directories using default or custom wordlists.  
3	Subdomain Finder: Searches for subdomains using a default or custom wordlist.  
4	Web Crawler (Spider): Crawls a target URL and lists discovered internal links.

Ensure the following dependencies and requirements are met:

Python 3.x, Wine (for compiling Windows binaries on Linux), PyInstaller (installed via Wine)

Modules: pyfiglet, rich, keylogger  
Install dependencies:

```
pip install pyfiglet rich
```

🔍 Wordlist Defaults

You should edit the paths of the downloaded wordlists in Default_paths.py:

DEFAULT_WORDLIST_DIR = "/your/path/to/directory-list.txt"

DEFAULT_WORDLIST_SUB = "/your/path/to/subdomains.txt"
