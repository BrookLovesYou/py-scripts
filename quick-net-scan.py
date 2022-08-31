#! /usr/bin/python3

import subprocess

ip = subprocess.check_output('hostname -I', shell=True, universal_newlines=True, encoding='utf-8')
snetip = (''.join(ip.rpartition('2')[:1])) + "0/24"
nmapout = subprocess.check_output('nmap {}'.format(snetip), shell=True, universal_newlines=True, encoding='utf-8')

print(nmapout)
