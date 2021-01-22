#! /usr/bin/env python3
# The line above makes this script run from shell.
# Just give it permission: $ sudo chmod +x this.py
# and run with:
# ./this.py

#from scapy.layers.inet import IP, TCP
from scapy.all import *
from scapy.contrib.bfd import BFD 
import codecs

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aux functions:

printr = lambda x : print(x.__repr__)
hexdec = lambda x : codecs.decode(x, 'hex')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mac_src = "64:32:a8:8c:f2:e9"
mac_dst = "01:80:C2:00:00:0E" # Multicast addr
lldp_frame_type = 0x88cc

ethernet_frame = Ether(src=mac_src, dst=mac_dst, type=lldp_frame_type)
lldpdu = '020704525400818711040405312f330602007800000000'

header = ethernet_frame / hexdec(lldpdu)
padding = Raw('0' * (512 - len(str(header))) )

pkt = header / padding

sendp(pkt, iface="wlo1")
