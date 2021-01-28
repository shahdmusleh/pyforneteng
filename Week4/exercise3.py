#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals
import re

with open('show_version.txt') as f:
    output = f.read()
os_version = re.search(r'^Cisco.*Version(.*),', output).group(1)
serial_num = re.search(r'^Pro.*ID(.*)', output, flags=re.M).group(1)
conf_reg = re.search(r'^Conf.*is(.*)', output, flags=re.M).group(1)

print('OS Version:{}\nSerial Number:{}\nConfig Register:{}'.format(
    os_version, serial_num, conf_reg))
