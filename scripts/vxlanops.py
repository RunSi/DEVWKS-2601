"""
Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Simon Hart"
__email__ = "sihart@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"


# Genie
# Import ops Base class so as to build Ops class
from genie.ops.base import Base

#
# Import Show nve neighbor and Show nve peers parsers
from iosxevxlan import ShowNveVni,ShowNvePeers,ShowNveIntf

#Create the Vxlan Ops Class
class Vxlan(Base):

    def learn(self, custom=None):


        # Capture output from ShowNveVni parser
        src = '[(?P<interf>.*)]'
        dest = 'info[(?P<interf>.*)]'
        req_keys = ['[VNI]','[Multicast-group]','[VNIstate]','[Mode]']
        for key in req_keys:
            self.add_leaf(cmd=ShowNveVni,
                          src=src + '[{}]'.format(key),
                          dest=dest + '[{}]'.format(key))


        # Capture ouput from ShowNvePeers parser
        src = '[(?P<nvename>.*)]'
        dest = 'info[(?P<nvename>.*)]'
        req_keys = ['[Peer-IP]','[Router-RMAC]','[Type]','[state]']
        for key in req_keys:
            self.add_leaf(cmd=ShowNvePeers,
                          src=src + '[{}]'.format(key),
                          dest=dest + '[{}]'.format(key))

        # Capture output from ShowNveIntf parser
        src = '[(?P<nveint>.*)]'
        #dest = 'info[(?P<nveint>Interface:\s[a-zA-Z0-9]+)]'
        dest = 'info[nve1]'
        req_keys = ['[nve.intf.if_encap]','[nve.intf.primary]','[nve.intf.source_intf]', '[nve.intf.vxdport]', '[nve.intf.vrf]']
        for key in req_keys:
            self.add_leaf(cmd=ShowNveIntf,
                          src=src + '[{}]'.format(key),
                          dest=dest + '[{}]'.format(key))
            print(dest + '[{}]'.format(key))

        #Add ops data to the Vxlan ojbect
        self.make()

