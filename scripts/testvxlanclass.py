
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