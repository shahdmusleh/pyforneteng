#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals
from pprint import pprint

vlan_list = []
with open('show_vlan.txt') as f:
    output = f.read()

for line in output.splitlines():
    if 'VLAN' in line or '-' in line or 'Et6' in line:
        continue
    vlan_id, vlan_name = line.split()[:2]
    vlan_list.append((vlan_id, vlan_name))
    
pprint(vlan_list)
