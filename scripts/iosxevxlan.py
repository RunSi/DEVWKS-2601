# Python
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

import re

# Metaparser
from genie.metaparser import MetaParser
from genie import parsergen
from genie.metaparser.util.schemaengine import Any, Optional



# parser utils
from genie.libs.parser.utils.common import Common


# =============================================
# Parser for 'show nve peers'
# =============================================

class ShowNvePeersSchema(MetaParser):
    """Schema for show nve peers
    """

    schema = {
        Any():{
        #    Any(): {
                'Interface': str,
                'Peer-IP': str,

                'Router-RMAC': str,
                'Type': str,
                Optional('Crap'): str,
                'UP time': str,
                'VNI': str,
                'eVNI': str,
               'flags': str,
               'state': str,
           },
        }
   #}


class ShowNvePeers(ShowNvePeersSchema):
# class ShowNvePeers():
    """ Parser for nve peers """

    def cli(self):
        # excute command to get output
        cmd = 'show nve peers'
        output = self.device.execute(cmd)

        header = ['Interface', 'VNI', 'Type', 'Peer-IP', 'Router-RMAC', 'eVNI', 'state', 'flags', 'UP time']

        result = parsergen.oper_fill_tabular(device_output=output, device_os='iosxe', header_fields=header, index=[0])

        return result.entries

# =============================================
# Parser for 'show nve vni'
# =============================================

class ShowNveVniSchema(MetaParser):
    """Schema for show vni peers
    """

    schema = {
        Any():{
        #    Any(): {
                'BD': str,
                'Interface': str,

                Optional('Mode'): str,
                'Multicast-group': str,
                Optional('Crap'): str,
                'VNI': str,
                'VNIstate': str,
                'cfg': str,
               'vrf': str
           },
        }
   #}

class ShowNveVni(ShowNveVniSchema):
# class ShowNveVni():
    """ Parser for nve vni """

    def cli(self):
        # excute command to get output
        cmd = 'show nve vni'

        output = self.device.execute(cmd)

        header = ['Interface', 'VNI', 'Multicast-group', 'VNI state', 'Mode', 'BD', 'cfg', 'vrf']
        label = ['Interface', 'VNI', 'Multicast-group', 'VNIstate', 'Mode', 'BD', 'cfg', 'vrf']


        result = parsergen.oper_fill_tabular(device_output=output, device_os='iosxe', header_fields=header, label_fields=label, index=[0])

        return result.entries


# =============================================
# Parser for 'show nve vni'
# =============================================

class ShowNveIntfSchema(MetaParser):
    """Schema for show vni peers
    """

    schema = {
        Any():{
                'nve.intf.if_encap': str,
                'nve.intf.primary': str,
                'nve.intf.source_intf': str,
                'nve.intf.ifname': str,
                'nve.intf.vxdport': str,
                'nve.intf.vrf': str

           },
        }

class ShowNveIntf(ShowNveIntfSchema):
# class ShowNveVni():
    """ Parser for nve vni """

    def cli(self):
        # excute command to get output
        show_cmds = {
            'iosxe': {
                'show_int': "show nve interface {}",
            }
        }

        regex = {

            'iosxe': {
                'nve.intf.if_encap': r'[a-zA-Z0-9\:\,\s]+Encapsulation:\s+(\w+),',
                'nve.intf.ifname': r'^Interface:\s(\w+)',
                'nve.intf.vxdport': r'[a-zA-Z0-9\:\,\s]+\sVxLAN\sdport:\s(\w+)',
                'nve.intf.source_intf': r'^source-interface:\s+(\w+)',
                'nve.intf.primary': r'[a-zA-Z0-9\:\-\s]+Loopback[a-zA-Z0-9\s\(]+\:(\d+\.\d+\.\d+\.\d+)',
                'nve.intf.vrf': r'[a-zA-Z0-9\:\-\s]+Loopback[a-zA-Z0-9\s\(]+\:\d+\.\d+\.\d+\.\d+\s+vrf:(\w+)\)',
            }
        }

        regex_tags = {
            'iosxe': ['nve.intf.if_encap', 'nve.intf.ifname', 'nve.intf.vxdport', 'nve.intf.source_intf',
                      'nve.intf.primary', 'nve.intf.vrf']
        }

        parsergen.extend(show_cmds=show_cmds, regex_ext=regex, regex_tags=regex_tags)

        attrValPairsToParse = [('nve.intf.if_encap', 'Vxlan')]
        pgfill = parsergen.oper_fill(
            self.device,
            ('show_int', ['nve1']),
            attrValPairsToParse,
            refresh_cache=True,
            regex_tag_fill_pattern='nve\.intf')
        pgfill.parse()

        return parsergen.ext_dictio
