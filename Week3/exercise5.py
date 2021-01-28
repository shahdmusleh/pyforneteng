#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals
import os

WINDOWS = False
base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

base_ip_addr = '10.10.100'
ip_addr_list = []

for last_octet in range(1, 254):
    ip_addr = base_ip_addr + '.' + str(last_octet)
    ip_addr_list.append(ip_addr)

for i, ip in enumerate(ip_addr_list):
    print('{} ---> {}'.format(i, ip))

new_list = ip_addr_list[2:6]

for new_ip in new_list:
    os.system('{} {}'.format(base_cmd_linux, new_ip))
