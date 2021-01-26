#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals

with open('show_ip_bgp_summ.txt') as f:
    output = f.readlines()

local_as_num = output[0].split()[-1]
bgp_peer_ip = output[-1].split()[0]

print('Local AS number: {} \nBGP peer IP address: {}'.format(
    local_as_num, bgp_peer_ip))
