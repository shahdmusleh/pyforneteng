#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals
import re
ipv6_list = []

with open('show_ipv6_intf.txt') as f:
    output = f.read()
match = re.search(r'^Ether.*?IPv6 address:(.*?)IPv6',
                  output, flags=re.S).group(1)
ipv6_addr = match.strip().splitlines()
for addr in ipv6_addr:
    addr = re.sub(r'\[VALID\]', '', addr)
    addr = addr.strip()
    ipv6_list.append(addr)

print(ipv6_list)
