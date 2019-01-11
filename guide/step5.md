### GENIE Non Tabular Parsing

Not all output from the device will be in tabular form.  Parsergen can deal with non tabular
returned data.  
Parsergen tries to match a given set of data using regular expressions that describe the values found
in the show command output.

Consider the following output from the _show nve interface nve 1_ .  
We shall parse the data to retrieve Source_Interface and Primary address based upon an encapsulation of Vxlan

```bash

Interface: nve1, State: Admin Up, Oper Up, Encapsulation: Vxlan,
BGP host reachability: Disable, VxLAN dport: 4789
VNI number: L3CP 0 L2CP 0 L2DP 1
source-interface: Loopback10 (primary:172.16.10.1 vrf:0)
```

There are two methods by which we can retrieve this data - Manual regular expressions and Markup

### Using Regular Expressions manually


To start make sure that your Python Virtual Environment is still running from step 4 and that you are in 
the scripts directory.
Initiate an iPython interactive session and intialise the testbed

```bash

$ ipython
```

```python
from pprint import pprint
from genie.conf import Genie
from genie import parsergen

testbed = Genie.init('sandbox_iosxe.yaml')
uut = testbed.devices.iosxe1
uut.connect()

```      

Create a dictionary of show commands. Only one show command for IOSXE in this instance

```python
show_cmds = {
     'iosxe': {
        'show_int' : "show nve interface {}",
     }
}
```

Create a dictionary of regular expressions to capture the elements required in the output. The 
example has regular expressions that will capture the encapsulation type, the source interface and the primary address.  
As useful tool for creating and validing python _re_ based regular expressions can be found here: [Pythex](https://pythex.org/)

```python
regex = {

    'iosxe': {
        'nve.intf.if_encap': r'[a-zA-Z0-9\:\,\s]+Encapsulation:\s+(\w+),',
        'nve.intf.source_intf': r'^source-interface:\s+(\w+)',
        'nve.intf.primary': r'[a-zA-Z0-9\:\-\s]+Loopback[a-zA-Z0-9\s\(]+\:(\d+\.\d+\.\d+\.\d+)'
     }
}

regex_tags = {
    'iosxe': ['nve.intf.if_encap',  'nve.intf.source_intf', 'nve.intf.primary']
    }

```



'Extend' the Parsergen Class to include the show commands and the regular expressions

```python
parsergen.extend(show_cmds=show_cmds, regex_ext=regex, regex_tags=regex_tags)
```

Now determine the parameters you wish to start the regex search on. The first item in the 
tuple is the key name of the regex value, the second item is the value being searched in this
case all interfaces with Vxlan encapsulation

```python
attrValPairsToParse = [('nve.intf.if_encap', 'Vxlan')]
```

Finally we create the object pgfill by calling the _parsergen.oper\_fill_ method is called.  The arguments in this method will
* determine the device to be called (uut)
* determine which show command to call from the key show_int and use nve1 as the interface name for the show command
* Provide the attribute value pairs to search on
* And use the defined regular expressions that begin with _nve.intf_

```python
pgfill = parsergen.oper_fill (
    uut,
    ('show_int', ['nve1']),
    attrValPairsToParse,
    refresh_cache=True,
    regex_tag_fill_pattern='nve\.intf')
```


Now enter the parse method for pgfill to populate parsergen ext_dictio attribute with the parsed items

```python
pgfill.parse()

pprint(parsergen.ext_dictio)

```

Disconnect from the device
```python
uut.disconnect()
```

---

**Full Script**

```python
from genie.conf import Genie
from genie import parsergen

from pprint import pprint


testbed = Genie.init('vagrant_single_ios.yaml')
uut = testbed.devices.iosxe1
uut.connect()


show_cmds = {
     'iosxe': {
        'show_int' : "show nve interface {}",
     }
}

regex = {

    'iosxe': {
        'nve.intf.if_encap': r'[a-zA-Z0-9\:\,\s]+Encapsulation:\s+(\w+),',
        'nve.intf.source_intf': r'^source-interface:\s+(\w+)',
        'nve.intf.primary': r'[a-zA-Z0-9\:\-\s]+Loopback[a-zA-Z0-9\s\(]+\:(\d+\.\d+\.\d+\.\d+)'
     }
}

regex_tags = {
    'iosxe': ['nve.intf.if_encap',  'nve.intf.source_intf']}

parsergen.extend(show_cmds=show_cmds, regex_ext=regex, regex_tags=regex_tags)

attrValPairsToParse = [('nve.intf.if_encap', 'Vxlan')]
pgfill = parsergen.oper_fill (
    uut,
    ('show_int', ['nve1']),
    attrValPairsToParse,
    refresh_cache=True,
    regex_tag_fill_pattern='nve\.intf')
pgfill.parse()
pprint(parsergen.ext_dictio)
```










[Beginning](../README.md)   [Back](./step4.md)  [Next](./step5b.md)