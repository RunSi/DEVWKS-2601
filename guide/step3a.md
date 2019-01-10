### GENIE OPS Library


The GENIE OPS Library is used to represent a device/feature's operational state/data through a Python Object. 
Each feature on each device is represented via a single Ops object instance, where state/status 
information is stored as an object attribute.

Ops objects are snapshots of a particular feature on a particular device at a specific time.
 
To demonstrate the power of the GENIE OPS library then please follow the sections below.

To start make sure that your Python Virtual Environment is still running from step 2 and that you are in 
the scripts directory.
Initiate an iPython interactive session

```bash

$ ipython
     
```

Import the Topology library and the Ops Interface Model(Class) and instantiate the topology object (referred to in this example as _testbed_)

```python
from pprint import pprint
from genie.conf import Genie

from genie.libs.ops.interface.iosxe.interface import Interface

testbed = Genie.init('vagrant_single_ios.yaml')

```

The commands above will:-

* Import the pprint library so as to 'pretty print' structured data to make it more easily readable
* From genie.conf import the Genie Class
* Import the Operational Model for IOSXE Interfaces
* Initiate the testbed file in order to interact with the testbed devices


Access to the devices needs to be established prior to sending any additional GENIE API calls to the device, leveraging
the topology _connect_ method. 

First make a reference to the topology device object  

As mentioned previously the device object has a method called connect.  Using the connect method will establish a connection to the device
using the connection method described in the topology yaml file, in this case _ssh_.  You will know that a connection is successful with the 
output from the device being displayed in the interactive session. Once connection is made the device will be prepared 
for further calls on the device.

```python
uut = testbed.devices.iosxe1

uut.connect()
```


---

### Learn the state of the interfaces on the device under test (iosxe1)

First an interface Ops object needs to instantiated.  The argument for instantiating the object is the device that is
being tested, defined earlier as _uut_.  

The _interface_ object that has been instantiated has a **learn** method.  The learn method will send several 
relevant show commands to an IOSXE device.  The output of the show commands will be parsed and collated and subsequently stored
as a single structured data entity(dictionary).

```python
interface = Interface(device=uut)

interface.learn()
```

The data that is parsed and collated is stored as a single entry under the _info_ attribute of the interface object.
  
To view all the returned data:-

```python
pprint(interface.info)
```

From the above output you should recognise that the data is now stored as a dictionary and thus the values can be 
retrieved by referencing the relevant key.

For example:-

```python
pprint(interface.info['nve1'])
```

And:-

```python
pprint(interface.info['nve1']['phys_address'])
```






[Beginning](../README.md)   [Back](./step2.md)  [Next](./step3b.md)