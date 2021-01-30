#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals
import re
import pdb


def normalize_mac(mac_address):
    mac_address = mac_address.upper()
    if re.search(r"[:-]", mac_address) is not None:
        new_mac = []
        octets = re.split(r"[:.-]", mac_address)
        for octet in octets:
            if len(octet) < 2:
                octet = octet.rjust(2, '0')
            new_mac.append(octet)
        new_mac = ':'.join(new_mac)
    elif '.' in mac_address and len(re.findall(r"\.", mac_address)) == 2:
        new_mac = []
        words = mac_address.split('.')
        for word in words:
            if len(word) < 4:
                word = word.rjust(4, '0')
            new_mac.append(word[:2])
            new_mac.append(word[2:])
        new_mac = ':'.join(new_mac)
    return(new_mac)


pdb.set_trace()
assert "01:23:00:34:04:56" == normalize_mac("123.34.456")
assert "AA:BB:CC:DD:EE:FF" == normalize_mac("aabb.ccdd.eeff")
assert "0A:0B:0C:0D:0E:0F" == normalize_mac("a:b:c:d:e:f")
assert "01:02:0A:0B:00:44" == normalize_mac("1:2:a:b:0:44")
assert "0A:0B:0C:0D:0E:0F" == normalize_mac("a-b-c-d-e-f")
assert "01:02:0A:0B:03:44" == normalize_mac("1-2-a-b-3-44")
print("Test cases passed")
