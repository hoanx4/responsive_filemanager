# Responsive Filemanager
Responsive FileManager 9.13.4 - 'path' Path Traversal

Exploit Title: Responsive FileManager 9.13.4 - 'path' Path Traversal
Date: 12/12/2018 (PoC)
Date: 04/01/2020 (Auto Exploit)
Exploit Author: SunCSR (Sun* Cyber Security Research)

Google Dork: intitle:"Responsive FileManager 9.x.x"

Vendor Homepage: http://responsivefilemanager.com/

Software Link: https://github.com/trippo/ResponsiveFilemanager/releases/tag/v9.13.4

Version: < 9.13.4

Tested on: Linux 64bit + Python3

```
#!/usr/bin/python3

Usage: python exploit.py [URL] [SESSION] [File Path]

python3 exploit.py http://local.lc:8081 PHPSESSID=hfpg2g4rdpvmpgth33jn643hq4 /etc/passwd
```
