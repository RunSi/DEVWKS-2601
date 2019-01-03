### GENIE OPS Library


The GENIE OPS Library is used to represent a devices/feature's operational state/data through a Python Object. 
Each feature on each device is represented via a single Ops object instance, where state/status 
information is stored as an object attribute.

Ops objects are snapshots of a particular feature on a particular device at a specific time.
 
To demonstrate the power of the GENIE OPS library then please follow the sections below.

To start make sure that your Python Virtual Environment is still running from step 2 and that you are in 
the scripts directory.
Initiate an iPython interactive session

```bash

$ ipython

Python 3.6.5 (default, Jun 17 2018, 12:13:06) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.2.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:        

```

Import the Topology library and the Ops Interface Library and instantiate the topology object (referred to in this example as _testbed_)

```python
import pprint
from genie.conf import Genie

from genie.libs.ops.interface.iosxe.interface import Interface

testbed = Genie.init('vagrant_multi_ios.yaml')

```

The commands above will:-

* Import the pprint library so as to 'pretty print' structured data to make it human readable
* Import the Genie.conf library
* Import the Operational data library for IOSXE Interfaces
* Initiate the testbed file in order to interact with the testbed devices


Access to the devices needs to be established prior to sending any additional GENIE API calls to the device, leveraging
the topology _connect_ method. 

First make a reference to the topology device object

```python
uut = testbed.devices.iosxe1
```

The device object has a method called connect.  Using the connect method will establish a connection to the device
using the connection method described in the topology yaml file.  You will know that a connection is successful with the 
output from the device being displayed in the interactive session.Once connection is made the device will be prepared 
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

The _interface_ object that has been instantiated has a **learn** method.  The learn method will send several 
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