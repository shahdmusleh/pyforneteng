#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals
import random


def rand_ip(base_ip='10.10.10'):
    rand_octet = str(random.randint(1, 254))
    return(base_ip + '.' + rand_octet)


print(rand_ip(), '\n')
print(rand_ip('172.16.16'), '\n')
print(rand_ip(base_ip='192.168.1'))
