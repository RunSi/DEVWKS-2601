### GENIE Parsergen


In addition to using the Ops package to retrieve and parse operational state of a device, the Genie Parsergen Packageprovides 
a one-step parsing mechanism that is capable of parsing dynamic tabular and non-tabular device outputs in a “noticeably” 
less lines of code compared to the standard parsing mechanisms.
The Genie Parsergen package is an extention of the top-level Cisco Genie automation package, based on Cisco pyATS framework.


This is useful where Genie does not have the library for the particular state you are looking to parse.
 As an example there is currently no Genie Ops library for NVE/VXLAN.  This gap can be overcome by creating the parser that can 
 then be leveraged by pyATS/GENIE.  
The object of the remaining exercises is to 
* Parse VXLAN relevant state
* Create an Ops library
* Run a pyATS easypy script to test condition of VXLAN state


###Tabular Parsing

The Genie Parsergen Package can deal with both Tabular and Non Tabular device output from a networking device. We 
shall initially explore Tabular parsing

Consider the output from the show command 'show nve vni'

```
Interface  VNI        Multicast-group VNI state  Mode  BD    cfg vrf                      
nve1       6001       N/A             Up         L2DP  1     CLI N/A 
```

As can been seen above this is a column based/tabular output.  In order to parse this output we need to instruct
parsergen as to the titles of the columns.  Follow the commands below to parse for the command 'show nve vni'

To start make sure that your Python Virtual Environment is still running from step 3 and that you are in 
the scripts directory.
Initiate an iPython interactive session

```bash

$ ipython

Python 3.6.5 (default, Jun 17 2018, 12:13:06) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.2.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:        

```

As in previous sections initiate the testbed topology and import the relevant libraries for this exercise

```python
import pprint
from genie.conf import Genie
from genie import parsergen

from genie.libs.ops.interface.iosxe.interface import Interface

testbed = Genie.init('vagrant_multi_ios.yaml')
uut = testbed.devices.iosxe1
uut.connect()

```

The testbed object 'uut.device' has a method of execute.  Execute will run the command on the device and return
a string as the result of the command

```python
output = uut.device.execute('show nve vni')
```

A list identifying the headers of the expected column output is created

```python
header = ['Interface', 'VNI', 'Multicast-group', 'VNI state', 'Mode', 'BD', 'cfg', 'vrf']
```

We will now use the parsergen oper_fill_tabular method to parse the string and store as structured data

```python
result = parsergen.oper_fill_tabular(device_output=output, device_os='iosxe', header_fields=header, index=[0])
```

Now print the structured data returned

```python
pprint.pprint(result.entries)
```

Determine the type of the result object entries attribute

```python
type(result.entries)
```

As you will see the returned data is now structured data in the form of a dictionary




[Beginning](../README.md)   [Back](step3b.md)  [Next](./step5.md)