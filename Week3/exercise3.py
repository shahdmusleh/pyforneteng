#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals

sys_name, port_id = [False, False]

with open('show_lldp_neighbors_detail.txt') as f:
    output = f.read()

for line in output.splitlines():
    if 'System Name' in line:
        sys_name = line.split()[2]
        print('System Name: {}'.format(sys_name))
    if 'Port id' in line:
        port_id = line.split()[2]
        print('Port id: {}'.format(port_id))
    if sys_name and port_id:
        break
