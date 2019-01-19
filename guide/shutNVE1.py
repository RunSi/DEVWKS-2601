from genie.conf import Genie
from genie.conf.base import Interface as Intf_conf

testbed = Genie.init('vagrant_single_ios.yaml')

uut = testbed.devices.iosxe1
uut.connect()

interface_cfg = Intf_conf(device=uut, name='NVE1')
interface_cfg.shutdown = True
interface_cfg.build_config()


uut.disconnect()