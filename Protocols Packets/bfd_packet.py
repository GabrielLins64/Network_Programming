#! /usr/bin/env python3

#from scapy.layers.inet import IP, TCP
from scapy.all import *
from scapy.contrib.bfd import BFD
import codecs

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Debug functions:

printr = lambda x : print(x.__repr__)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ethernet_frame = Ether(src="24:cb:cb:a4:eb:20", dst="ff:ff:ff:ff:ff:ff")
ip_packet = IP(src="192.168.15.38", dst="192.168.15.1")
udp_packet = UDP(dport=3784, sport=1024)
#bfd_packet = BFD(my_discriminator=0x00000001, your_discriminator=0x00000000)
raw_data = Raw(load="Teste gabriel-lins")

bfd_packet = "204405210000000100000000000f4240000f424000000000010902736563726574"
bfd_packet = codecs.decode(bfd_packet, 'hex')

pkt = ethernet_frame / ip_packet / udp_packet / bfd_packet / raw_data

sendp(pkt, iface="enp3s0")
