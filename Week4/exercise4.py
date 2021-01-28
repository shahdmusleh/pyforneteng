#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals
import re

show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''
match = re.search(r'^Cisco (?P<model>\S+) \(M.*with (?P<memory>\S+) bytes',
                  show_version, flags=re.M).groupdict()
print(match)
