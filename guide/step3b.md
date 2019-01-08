### Genie Ops continued

**Partial retrieval of Ops data**

Rather than retrieving the entire state you can choose to only save the attributes you require for the interface.  
For example we only wish to retrieve the Mac Addresses of the interfaces.  To achieve this

```python
interface = Interface(device=uut, attributes=['info[(.*)][mac_address]'])
```

Now 'relearn' the interface object and display the output

```python
interface.learn()

pprint.pprint(interface.info)

```

Now try and find other parameters from the interface object to learn and display (for example, 'mtu', 'bandwidth')


MORE TO ADD  - Do Diff here


---

**Full Script**

```python

import pprint
from genie.conf import Genie

from genie.libs.ops.interface.iosxe.interface import Interface

testbed = Genie.init('vagrant_multi_ios.yaml')

uut = testbed.devices.iosxe1

uut.connect()

interface = Interface(device=uut)

interface.learn()

pprint.pprint(interface.info)
pprint.pprint(interface.info['nve1'])


interface = Interface(device=uut, attributes=['info[(.*)][mac_address]'])

interface.learn

pprint.pprint(interface.info)

```

[Beginning](../README.md)   [Back](./step3a.md)  [Next](./step4.md)