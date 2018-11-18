
#Import Genie libraries
from genie.conf import Genie
from genie import parsergen

from pprint import pprint

#Create Testbed Object with Genie
testbed = Genie.init('vagrant_multi_ios.yaml')

#Create Device Object
uut = testbed.devices.iosxe1

#Use connect method to initiate connection to the device under test
uut.connect()

#Execute command show nve nvi on connected device
output = uut.device.execute('show nve vni')

#Create list of Header names of the table from show nve nvi - must match exactly to that which is output on cli
header = ['Interface', 'VNI', 'Multicast-group', 'VNI state', 'Mode', 'BD', 'cfg', 'vrf']

#Use Parsergen to parse the output and create structured output (dictionary of operational stats)
result = parsergen.oper_fill_tabular(device_output=output, device_os='iosxe', header_fields=header, index=[0])

#Pretty Print the Dictionary
pprint(result.entries)