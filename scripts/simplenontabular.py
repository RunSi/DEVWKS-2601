from genie.conf import Genie
from genie import parsergen
from pprint import pprint

#open marked up text file and read into variable
f = open('markup.txt', 'r')
markedupIOSX = f.read()

#initiate testbed
testbed = Genie.init('vagrant_multi_ios.yaml')
uut = testbed.devices.iosxe1
uut.connect()

#extend parsergen markup with text file indicating elements to parse
parsergen.extend_markup(markedupIOSX)

#identify which parsed element to check as true
attrValPairsToCheck = [
    ('nve.intf.encap', 'Vxlan'),]

#parsergen will connect to device and issue show nve interface nve1
#Will check for elements to be parsed and create a dictionary
pgfill = parsergen.oper_fill(device=uut,
    show_command=\
('show_nve_interface', [], {'ifname':'nve1'}),
attrvalpairs=attrValPairsToCheck,
refresh_cache=True, regex_tag_fill_pattern='nve\.intf')

result = pgfill.parse()
print(result)
print("Parsing details : {}".format(parsergen.ext_dictio[uut.name]))
pprint(parsergen.ext_dictio)