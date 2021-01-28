#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
show_version = show_version.strip()
show_version = show_version.split()
model = show_version[1]
serial_num = show_version[2]
print('Is cisco in the model? {}'.format('cisco' in model.lower()))
print('Is 881 in the model? {}'.format('881' in model))
print()
print(model)
print(serial_num)
