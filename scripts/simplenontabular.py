from genie.conf import Genie
from genie import parsergen


from pprint import pprint

f = open('markup.txt', 'r')

markedupIOSX = f.read()

#Create Testbed Object with Genie
testbed = Genie.init('vagrant_multi_ios.yaml')

#Create Device Object
uut = testbed.devices.iosxe1

#Use connect method to initiate connection to the device under test
uut.connect()

parsergen.extend_markup(markedupIOSX)

attrValPairsToCheck = [
    ('nve.intf.encap', 'Vxlan'),]

pgfill = parsergen.oper_fill(device=uut,
    show_command=\
('show_nve_interface_<WORD>', [], {'ifname':'nve1'}),
attrvalpairs=attrValPairsToCheck,
refresh_cache=True, regex_tag_fill_pattern='nve\.intf')

result = pgfill.parse()
print(result)
print("Parsing details : {}".format(parsergen.ext_dictio[uut.name]))
pprint(parsergen.ext_dictio)