from genie.conf import Genie
from genie import parsergen

from pprint import pprint


testbed = Genie.init('vagrant_multi_ios.yaml')
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
        'nve.intf.source_intf': r'^source-interface:\s+(\w+)',
        'nve.intf.primary': r'source\-interface:[a-zA-Z0-9\s]+\(primary:([A-Fa-f0-9:\.]+)',
     }
}

regex_tags = {
    'iosxe': ['nve.intf.if_encap',  'nve.intf.source_intf', 'nve.intf.primary']
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