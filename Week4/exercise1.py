#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals

net_device = {'ip_addr': '192.168.1.2', 'vendor': 'cisco',
              'username': 'user', 'password': 'password'}

if net_device['vendor'] == 'cisco':
    net_device['platform'] = 'ios'
elif net_device['vendor'] == 'juniper':
    net_device['platform'] = 'junos'

bgp_fields = {'bgp_as': '65101', 'peer_as': '65102', 'peer_ip': '172.16.1.1'}
net_device.update(bgp_fields)

for key in net_device:
    print(key)

print('-'*60)

for key, value in net_device.items():
    print(key, '--->', value)
