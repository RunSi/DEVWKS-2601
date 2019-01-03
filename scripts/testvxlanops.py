
# Genie
# Import ops Base class so as to build Ops class
from genie.ops.base import Base

#
# Import Show nve neighbor and Show nve peers parsers
from testvxlanclass import ShowNveVni,ShowNvePeers

#Create the Vxlan Ops Class
class Vxlan(Base):

    def learn(self, custom=None):


        # Capture ouptut frmo ShowNveVni parser
        src = '[(?P<interface>.*)]'
        dest = 'info[(?P<interface>.*)]'
        req_keys = ['[VNI]','[Multicast-group]','[VNIstate]','[Mode]']
        for key in req_keys:
            self.add_leaf(cmd=ShowNveVni,
                          src=src + '[{}]'.format(key),
                          dest=dest + '[{}]'.format(key))


        # Capture ouptut from ShowNveVni parser
        src = '[(?P<nvename>.*)]'
        dest = 'info[(?P<nvename>.*)]'
        req_keys = ['[Peer-IP]','[Router-RMAC]','[Type]','[state]']
        for key in req_keys:
            self.add_leaf(cmd=ShowNvePeers,
                          src=src + '[{}]'.format(key),
                          dest=dest + '[{}]'.format(key))

        #Add ops data to the Vxlan ojbect
        self.make()