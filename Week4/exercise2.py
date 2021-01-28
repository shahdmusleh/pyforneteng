#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals
from pprint import pprint

houston_dc_rtr = ['10.1.10.1', '10.1.20.1', '10.1.30.1', '10.1.40.1',
                  '10.1.50.1', '10.1.60.1', '10.1.70.1', '10.1.10.1', '10.1.20.1', '10.1.30.1']
atlanta_dc_rtr = ['10.1.10.1', '10.1.20.1', '10.1.40.1', '10.1.80.1',
                  '10.1.100.1', '10.1.120.1', '10.1.130.1', '10.1.140.1']
chicago_dc_rtr = ['10.1.10.1', '10.1.20.1', '10.1.120.1',
                  '10.1.130.1', '10.1.160.1', '10.1.170.1', '10.1.180.1', '10.1.190.1']
houston_set = set(houston_dc_rtr)
atlanta_set = set(atlanta_dc_rtr)
chicago_set = set(chicago_dc_rtr)

print('IP addresses duplicated between Houston and Atlanta: {}'.format(
    houston_set & atlanta_set))
print('IP addresses duplicated in three sites: {}'.format(
    houston_set & atlanta_set & chicago_set))
print('IP addresses unique in Chicago: {}'.format(
    chicago_set - atlanta_set - houston_set))
