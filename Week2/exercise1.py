#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals

f = open('show_version.txt')
output = f.read()
print(output, '\n')
print(type(output))
f.close()
print('-'*60,'\n')

with open('show_version.txt') as f:
    output = f.readlines()
print(output, '\n')
print(type(output))
