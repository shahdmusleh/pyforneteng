#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals
found1, found30 = [False, False]

with open('show_arp.txt') as f:
    output = f.read()

for line in output.splitlines():
    if 'Protocol' in line:
        continue
    ip_addr = line.split()[1]
    mac_addr = line.split()[3]
    if ip_addr == '10.220.88.1':
        found1 == True
        print('Default gateway IP/MAC: {}/{}'.format(ip_addr, mac_addr))
    if ip_addr == '10.220.88.30':
        found30 = True
        print('Arista3 IP/MAC: {}/{}'.format(ip_addr, mac_addr))
    if found1 and found30:
        break
