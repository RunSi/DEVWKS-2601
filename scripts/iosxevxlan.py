
from genie import parsergen

class ShowNvePeers():
    """ Parser for nve peers """

    def cli(self):
        # excute command to get output
        cmd = 'show nve peers'
        output = self.device.execute(cmd)

        header = ['Interface', 'VNI', 'Type', 'Peer-IP', 'Router-RMAC', 'eVNI', 'state', 'flags', 'UP time']

        result = parsergen.oper_fill_tabular(device_output=output, device_os='iosxe', header_fields=header, index=[0])

        return result.entries


class ShowNveVni():
    """ Parser for nve vni """

    def cli(self):
        # excute command to get output
        cmd = 'show nve vni'

        output = self.device.execute(cmd)

        header = ['Interface', 'VNI', 'Multicast-group', 'VNI state', 'Mode', 'BD', 'cfg', 'vrf']
        label = ['Interface', 'VNI', 'Multicast-group', 'VNIstate', 'Mode', 'BD', 'cfg', 'vrf']


        result = parsergen.oper_fill_tabular(device_output=output, device_os='iosxe', header_fields=header, label_fields=label, index=[0])

        return result.entries