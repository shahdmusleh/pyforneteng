#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals

ip_addr = ['192.168.1.1', '192.168.1.2',
           '192.168.1.3', '192.168.1.4', '192.168.1.5']

ip_addr.append('192.168.1.254')
ip_addr.extend(['192.168.1.6', '192.168.1.7'])
ip_addr = ip_addr + ['8.8.8.8', '4.4.2.2']

print(ip_addr)
print(ip_addr[0])
print(ip_addr[-1])

ip_addr.pop()
ip_addr.pop(-1)

ip_addr[0] = '2.2.2.2'
print(ip_addr[0])
