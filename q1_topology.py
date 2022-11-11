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

        # switches
        switch_r1 = self.addSwitch('r1')

        # links
        self.addLink(host_A, switch_r1, bw=500, delay='0', loss = 0)
        self.addLink(switch_r1, host_B, bw=500, delay='0', loss = 0)


if __name__ == '__main__':
    setLogLevel( 'info' )
    startNetwork()
