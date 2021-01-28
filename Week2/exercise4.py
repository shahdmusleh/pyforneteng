#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals

with open("show_ip_int_brief.txt") as f:
    output = f.readlines()

fast_eth4 = output[5]
intf_name, ip_address = fast_eth4.split()[:2]
fast_eth4_tuple = (intf_name, ip_address)
print(fast_eth4_tuple)
