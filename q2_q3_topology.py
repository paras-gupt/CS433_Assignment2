from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController, OVSBridge
from mininet.link import TCLink

def startNetwork():

    topo = cutomTopology()
    net = Mininet( topo=topo, controller=OVSController,switch=OVSBridge, link=TCLink)
    net.start()
    CLI( net )
    net.stop()

class cutomTopology( Topo ):

    def build( self, **_kwargs ):

        # host nodes 
        host_A = self.addHost('A', ip='192.0.0.0/8')
        host_B = self.addHost('B', ip='192.0.0.1/8')
        host_C = self.addHost('C', ip='192.0.0.2/8')
        host_D = self.addHost('D', ip='192.0.0.3/8')

        # switches
        switch_r1 = self.addSwitch('r1')
        switch_r2 = self.addSwitch('r2')

        # links
        self.addLink(host_A, switch_r1, bw=1000, delay='1ms', loss = 0)
        self.addLink(host_D, switch_r1, bw=1000, delay='1ms', loss = 0)
        self.addLink(switch_r2, host_B, bw=1000, delay='1ms', loss = 0)
        self.addLink(switch_r2, host_C, bw=1000, delay='5ms', loss = 0)
        self.addLink(switch_r1, switch_r2, bw=500, delay='10ms', loss = 0)


if __name__ == '__main__':
    setLogLevel( 'info' )
    startNetwork()
