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

from genie.conf import Genie
from genie import parsergen
import logging

from pprint import pprint


testbed = Genie.init('sandbox_iosxe.yaml')
uut = testbed.devices.iosxe1
uut.connect()


show_cmds = {
     'iosxe': {
        'show_int' : "show nve interface {}",
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
pgfill = parsergen.oper_fill (
    uut,
    ('show_int', ['nve1']),
    attrValPairsToParse,
    refresh_cache=True,
    regex_tag_fill_pattern='nve\.intf')
pgfill.parse()
pprint(parsergen.ext_dictio)


uut.disconnect()