#!/usr/bin/python

"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import sys

def emptyNet():

    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller )
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    net.addController( 'c0' )
    
    pre = 1
    for i in range(0, y):
        info( '*** Adding hosts h'+str(pre)+' h'+str(pre+1)+'\n' )
        h_odd = net.addHost( 'h'+str(pre), ip='11.0.0.1' )
        pre = pre+1
        h_even = net.addHost( 'h'+str(pre), ip='10.0.0.1' )
        pre = pre+1
        info( '*** Adding switch s'+str(i+1)+'\n' )
        switch = net.addSwitch( 's'+str(i+1) )

        info( '*** Creating links\n' )
        info( '*** Bandwidth = 1Mbps for h'+str(pre-2)+'\n' )
        conf1 = net.addLink( h_odd, switch )
        conf1.intf1.config(bw=1)
        info( '*** Bandwidth = 2Mbps for h'+str(pre-1)+'\n' )
        conf2 = net.addLink( h_even, switch )
        conf2.intf1.config(bw=1)

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
