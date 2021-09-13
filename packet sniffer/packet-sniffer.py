#!/usr/bin/python3
print("Use Sudo")

from datetime import datetime 
import sys
import subprocess 
from scapy.all import *

net_iface = input("Enter interface name: ")


subprocess.call(["ifconfig",net_iface,"promisc"]) 

num_of_pkt = int(input("Enter the packet count you want to capture"))

time_sec =int(input("Enter the time how long(in sec) run to capture"))

proto = input("Enter the protocol(arp | icmp |all)")


def logs(packet):
	print(f"SRC_MAC: {str(packet[0].src)} DEST_MAC: {str(packet[0].dst)}")


if proto == "all":
	sniff(iface = net_iface ,count = num_of_pkt, timeout = time_sec, prn=logs )
elif proto == "arp":
	sniff(iface = net_iface, count = num_of_pkt,timout = time_sec , prn = logs , filter = proto)
elif proto == "icmp":
	sniff(iface = net_iface, count = num_of_pkt,timout = time_sec , prn = logs , filter = proto) 
else:
	print("Wrong protocol")

