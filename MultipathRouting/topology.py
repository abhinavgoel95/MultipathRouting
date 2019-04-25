#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)

    #s1.cmd("ovs-vsctl -- set port s1-eth1 qos=@newqos -- --id=@newqos create qos type=linux-htb queues=0=@q0,1=@q1 -- --id=@q0 create queue other-config:min-rate=0 other-config:max-rate=7000000 -- --id=@q1 create queue other-config:min-rate=0 other-config:max-rate=3000000")
    #s2.cmd("ovs-vsctl -- set port s1-eth4 qos=@newqos -- --id=@newqos create qos type=linux-htb queues=0=@q0,1=@q1 -- --id=@q0 create queue other-config:min-rate=0 other-config:max-rate=7000000 -- --id=@q1 create queue other-config:min-rate=0 other-config:max-rate=3000000")
    #s3.cmd("ovs-vsctl -- set port s1-eth4 qos=@newqos -- --id=@newqos create qos type=linux-htb queues=0=@q0,1=@q1 -- --id=@q0 create queue other-config:min-rate=0 other-config:max-rate=7000000 -- --id=@q1 create queue other-config:min-rate=0 other-config:max-rate=3000000")
    #s4.cmd("ovs-vsctl -- set port s1-eth4 qos=@newqos -- --id=@newqos create qos type=linux-htb queues=0=@q0,1=@q1 -- --id=@q0 create queue other-config:min-rate=0 other-config:max-rate=7000000 -- --id=@q1 create queue other-config:min-rate=0 other-config:max-rate=3000000")
    #s5.cmd("ovs-vsctl -- set port s1-eth4 qos=@newqos -- --id=@newqos create qos type=linux-htb queues=0=@q0,1=@q1 -- --id=@q0 create queue other-config:min-rate=0 other-config:max-rate=7000000 -- --id=@q1 create queue other-config:min-rate=0 other-config:max-rate=3000000")

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(h1, s1)
    s1s2 = {'bw':10}
    net.addLink(s1, s2, cls=TCLink , **s1s2)
    s2s5 = {'bw':10}
    net.addLink(s2, s5, cls=TCLink , **s2s5)
    net.addLink(s5, h4)
    s1s3 = {'bw':10}
    net.addLink(s1, s3, cls=TCLink , **s1s3)
    s3s4 = {'bw':10}
    net.addLink(s3, s4, cls=TCLink , **s3s4)
    s4s5 = {'bw':10}
    net.addLink(s4, s5, cls=TCLink , **s4s5)
    net.addLink(s5, h3)
    net.addLink(h2, s1)
    net.addLink(s6, s4)
    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s3').start([c0])
    net.get('s2').start([c0])
    net.get('s1').start([c0])
    net.get('s5').start([c0])
    net.get('s4').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

