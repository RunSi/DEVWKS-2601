### GENIE Parsergen


In addition to using the Ops package to retrieve and parse operational state of a device, the Genie Parsergen Class provides 
a one-step parsing mechanism that is capable of parsing dynamic tabular and non-tabular device outputs in a “noticeably” 
less lines of code compared to standard parsing mechanisms.  


The Parsergen Class is particularly useful where Genie Ops does not have a model for the particular state you are 
looking to parse.  
As an example there is currently no Genie Ops Model for NVE/VXLAN.  This gap can be overcome by creating the parser that can 
 then be leveraged by pyATS/GENIE.  
 
The object of the remaining exercises is to 
* Parse VXLAN relevant state
* Create an Ops library
* Run a pyATS easypy script to test condition of VXLAN state


### Tabular Parsing

The Genie Parsergen Class can deal with both Tabular and Non Tabular device output from a networking device. We 
shall initially explore Tabular parsing

Consider the output from the show command 'show nve vni'

```
Interface  VNI        Multicast-group VNI state  Mode  BD    cfg vrf                      
nve1       6001       N/A             Up         L2DP  1     CLI N/A 
```

As can been seen above this is a column based/tabular output.  In order to parse this output we need to instruct
parsergen as to the titles of the columns.  Follow the commands below to parse the command 'show nve vni'

To start make sure that your Python Virtual Environment is still running from step 3 and that you are in 
the scripts directory.
If not already running initiate an iPython interactive session

```bash

$ ipython

```

As in previous sections initiate the testbed topology and import the relevant libraries for this exercise

```python
from pprint import pprint
from genie.conf import Genie
from genie import parsergen

testbed = Genie.init('vagrant_single_ios.yaml')
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
pprint(result.entries)
```

Determine the type of the result object entries attribute

```python
type(result.entries)
```

As you will see the returned data is now structured data in the form of a dictionary

Disconnect from the device
```python
uut.disconnect()
```

---

**Full Script**

```python

#Import Genie libraries
from genie.conf import Genie
from genie import parsergen
import re

from pprint import pprint

#Create Testbed Object with Genie
testbed = Genie.init('vagrant_single_ios.yaml')

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
```


[Beginning](../README.md)   [Back](step3b.md)  [Next](./step5.md)