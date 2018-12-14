### GENIE OPS Library


The GENIE OPS Library is used to represent a devices/feature's operational state/data through a Python Object. 
Each feature on each device is represented via a single Ops object instance, where state/status 
information is stored as an object attribute.
 
To demonstrate the power of the GENIE OPS library then please follow the sections below.

To start make sure that your Python Virtual Environment has been instantiated and start a Python Session

```bash

$ cd ~/DEVWKS-2601/
$ source venv/bin/activate 
$ cd scripts/
$ python

Python 3.6.5 (default, Jun 17 2018, 12:13:06) 
[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 

```

Import the Topology library and the Ops Interface Library and instantiate the topology object (referred to in this example as _testbed_)

```python
import pprint
from genie.conf import Genie

from genie.libs.ops.interface.iosxe.interface import Interface

testbed = Genie.init('vagrant_multi_ios.yaml')

```

Access to the devices needs to be established prior to sending any additional GENIE API calls to the device, leveraging
the topology _connect_ method. 

First make a reference to the topology device object

```python
uut = testbed.devices.iosxe1
```

The device object has a method called connect.  Using the connect method will establish a connection to the device
using the connection method described in the topology yaml file.  Once connection is made the device will be prepared 
for further calls on the device.

```python
uut.connect()
```

### Learn the state of the interfaces on the device under test (iosxe1)

First an interface Ops object needs to instantiated.  The argument for instantiating the object is the device that is
being tested.

```python
interface = Interface(device=uut)
```

The _interface_ object that has been instantiated has a **learn** method.  The learn method will send several show commands
relevant show commands to an IOSXE device.  The output of the show commands will be stored as structured data as an
attribute (info) of the interface object.

```python
interface.learn()
```

The data returned and stored within the info attribute (interface.info), is a dictionary derived from the genie ops
class.  
To view the returned data:-

```python
pprint.pprint(interface.info)
```

View the data for just one interface

```python
pprint.pprint(interface.info['nve1'])
```






[Beginning](../README.md)   [Back](./step2.md)  [Next](./step3b.md)