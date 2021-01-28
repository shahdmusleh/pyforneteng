#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals
from pprint import pprint

with open('show_arp.txt') as f:
    output = f.readlines()
output = output[1:]
pprint(output)

output.sort()

first_three_entries = output[:3]
new_str = '\n'.join(first_three_entries)

f = open('arp_entries.txt', 'w')
f.write(new_str)
