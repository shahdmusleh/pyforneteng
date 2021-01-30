#!usr/bin/ python3.8

from __future__ import print_function, unicode_literals

# Part a


def ssh_conn(ip_addr, username, password):
    print("IP address: {}\nUsername: {}\nPassword: {}\n".format(
        ip_addr, username, password))


ssh_conn('192.168.1.1', 'cisco', 'cisco123')
ssh_conn(username='cisco', password='cisco123', ip_addr='192.168.1.1')
ssh_conn('192.168.1.1', password='cisco123', username='cisco')

# Part b


def ssh_conn2(ip_addr, username, password, device_type='cisco_ios'):
    print("IP address: {}\nUsername: {}\nPassword: {}\nDevice type: {}\n".format(
        ip_addr, username, password, device_type))


ssh_conn2('192.168.1.1', 'admin', 'admin123', 'cisco_ios')
ssh_conn2('192.168.1.1', 'admin', 'admin123')

my_dict = {'ip_addr': '192.168.1.1', 'username': 'admin',
           'password': 'admin123', 'device_type': 'cisco_ios'}
ssh_conn2(**my_dict)
