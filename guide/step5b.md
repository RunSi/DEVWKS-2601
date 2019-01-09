### Using Markup Text to parse Non Tabular Output

Rather than explicitly defining regular expressions for each item to retrieve an alternative
we can use a special CLI command markup format that will automatically generate the regular
expressions.

If you have an iPython session running. Close and restart iPython

Initiate an iPython interactive session and intialise the testbed

```bash

$ ipython

import pprint
from genie.conf import Genie
from genie import parsergen

from genie.libs.ops.interface.iosxe.interface import Interface

testbed = Genie.init('vagrant_multi_ios.yaml')
uut = testbed.devices.iosxe1
uut.connect()

```      

Enter the following to assign the _marked up_ string to the variable markedupIOSX

```python
markedupIOSX = '''
OS: iosxe
CMD: show_nve_interface
SHOWCMD: show nve interface {ifname}
PREFIX: nve.intf
ACTUAL:

Interface: nve1, State: Admin Up, Oper Up, Encapsulation: Vxlan,
BGP host reachability: Disable, VxLAN dport: 10000
VNI number: L3CP 0 L2CP 0 L2DP 1
source-interface: Loopback10 (primary:1.1.1.1 vrf:22)

MARKUP:
Interface: XW<ifname>Xnve1, State: Admin XW<state>XUp, Oper Up, Encapsulation: XW<encap>XVxlan,
BGP host reachability: Disable, VxLAN dport: XN<udp_port>X1000
VNI number: L3CP 0 L2CP 0 L2DP 1
source-interface: XW<source_interface>XLoopback0 (primary:XA<primary_address>X1.1.1.1 vrf:XN<VRF>X22)'''
```
You will notice in the string that there are some key components

**OS:** Define the operating system being used  
**CMD:** Used by parsergen as the dict key for the _SHOWCMD_  
**SHOWCMD:** The actual show command to be issued  
**PREFIX** Will be used to prefix the keys for each item parsed  
**ACTUAL** Output expected from the device (optional)  
**MARKUP** The Output with markup added. Will be used to identify items to parse

The Markup itself begins and ends with **X** with the key name inbetween.  For example
**XW\<ifname>X**  will assign a value to the key nve.intf.**ifname**

Full list of Markup tags are included at the bottom of this file.

The remaining commands are similar to those used for parsing with regular expressions

'Extend' the parsergen library to include the show commands and the regular expressions
```python
parsergen.extend_markup(markedupIOSX)
```

Now determine the parameters you wish to start the regex search on. The first item in the 
tuple is the key name of the regex value, the second item is the value being searched. In this instance
only nve interfaces that have a Vxlan encapsulation are being considered

```python
attrValPairsToCheck = [('nve.intf.encap', 'Vxlan'),]
```

Calls the parsergen.oper_fill method in order to create a dictionary of the parsed output. 

```python
pgfill = parsergen.oper_fill(device=uut,
                             show_command=('show_nve_interface', [], {'ifname':'nve1'}),
                             attrvalpairs=attrValPairsToCheck,
                             refresh_cache=True, 
                             regex_tag_fill_pattern='nve\.intf')
```
Now call the parse method for the object pgfill

```python
pgfill.parse()
```

Print the parsed output

```python
print(parsergen.ext_dictio)
```


---


**Mark Up Reference**

The following are the available values for x in the XxX notation:

* A - IPv4 or IPv6 address.  
* B - Value terminated with a close brace, bracket, or parenthesis.
* C - Value terminated with a comma.
* F - Floating point number.
* H - Hexidecimal number.
* I - Interface name.
* M - Mac address.
* N - Decimal number.
* R - everything else to the newline.
* P - IPv4 or IPv6 prefix.
* Q - Value terminated by a double quote.
* S - Non-space value.
* T - Time (00:00:00)
* W - A word.

---

**Full Script**

```python
from genie.conf import Genie
from genie import parsergen
from pprint import pprint

#open marked up text file and read into variable
f = open('markup.txt', 'r')
markedupIOSX = f.read()

#initiate testbed
testbed = Genie.init('vagrant_multi_ios.yaml')
uut = testbed.devices.iosxe1
uut.connect()

#extend parsergen markup with text file indicating elements to parse
parsergen.extend_markup(markedupIOSX)

#identify which parsed element to check as true
attrValPairsToCheck = [
    ('nve.intf.encap', 'Vxlan'),]

#parsergen will connect to device and issue show nve interface nve1
#Will check for elements to be parsed and create a dictionary
pgfill = parsergen.oper_fill(device=uut,
    show_command=\
('show_nve_interface', [], {'ifname':'nve1'}),
attrvalpairs=attrValPairsToCheck,
refresh_cache=True, regex_tag_fill_pattern='nve\.intf')

pgfill.parse()
pprint(parsergen.ext_dictio)
```

[Beginning](../README.md)   [Back](./step5.md)  [Next](./step6.md)