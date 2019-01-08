### GENIE Non Tabular Parsing

Not all output from the device will be in tabular form.  Parsergen can deal with non tabular
returned data.  
Parsergen tries to match a given set of data using regular expressions that describe the values found
in the show command output.

Consider the following output from the _show nve interface nve 1_ .  
We shall parse the data to retrieve the VxLAN dport and the Source-Interface

```python

Interface: nve1, State: Admin Up, Oper Up, Encapsulation: Vxlan,
BGP host reachability: Disable, VxLAN dport: 4789
VNI number: L3CP 0 L2CP 0 L2DP 1
source-interface: Loopback10 (primary:172.16.10.1 vrf:0)
```
There are two methods by which we can retrieve this data

**Using Regular Expressions**


To start make sure that your Python Virtual Environment is still running from step 4 and that you are in 
the scripts directory.
Initiate an iPython interactive session and intialise the testbed

```bash

$ ipython

Python 3.6.5 (default, Jun 17 2018, 12:13:06) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.2.0 -- An enhanced Interactive Python. Type '?' for help.


import pprint
from genie.conf import Genie
from genie import parsergen

from genie.libs.ops.interface.iosxe.interface import Interface

testbed = Genie.init('vagrant_multi_ios.yaml')
uut = testbed.devices.iosxe1
uut.connect()

```      

Create a dictionary of show commands. Only one show command for IOSXE in this instance

```python
show_cmds = {
     'iosxe': {
        'show_intf' : "show interface {}",
     }
}
```

Create a dictionary of regular expressions to capture the elements required in the output

```python
regex = {

    'iosxe': {
        'show.intf.if_name'  : r'([-A-Za-z0-9\._/:]+)',
        'show.intf.encap': r'\s+Encapsulation\s+(\w+),',
     }
}
```

'Extend' the parsergen library to include the show commands and the regular expressions

```python
parsergen.extend(show_cmds=show_cmds, regex_ext=regex)
```

Now determine the parameters you wish to start the regex search on. The first item in the 
tuple is the key name of the regex value, the second item is the value being searched 

```python
attrValPairsToParse = [('show.intf.if_name', 'GigabitEthernet1')]
```








[Beginning](../README.md)   [Back](./step4.md)  [Next](./step5b.md)