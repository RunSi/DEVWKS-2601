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

pprint(interface.info)

```

Now try and find other parameters from the interface object to learn and display (for example, 'mtu', 'bandwidth')


---

**Verify State**

A very useful feature of the Ops object is to verify the condition of a particular state.  

The code below creates a function that checks the current oper_status of GigabitEthernet3.  

If the oper_status is up, then the verification is successful it will print that Gig3 is up and return to the main body of the
code.  

If the oper_status is down it will learn the interface state 3 more times with a sleep interval of 3 seconds, if after 3 attempts
the interface is still down then an Exception will be raised.

Enter the code as is below to your iPython session

````python
interface = Interface(device=uut)

def verify_interface_status(obj):
    if obj.info['GigabitEthernet3'].get('oper_status', None) and\
       obj.info['GigabitEthernet3']['oper_status'] == 'up':
       print('\n\nGig 3 is up')
       return
    raise Exception('Gig 3 is currently down')
    
interface.learn_poll(verify=verify_interface_status, sleep=3, attempt=3)

````
 
If the lab you are using is the Sandbox - ssh cisco@10.10.20.48   password cisco_1234!  

If the lab you are using is a local vagrant machine - ssh -p 3122 vagrant@127.0.0.1 vagrant
  


```bash

conf t
interface GigabitEthernet3
shutdown
```
Now rerun the above code and observe the results

---

**Compare State**

In order to determine what state has changed over time we can compare 'snapshots'.  Consider that each time you 
initiate the learn method, you are effectively taking a snapshot of current state.  

The code below will demonstrate, please enter into iPython:-

```python
interface_before = Interface(device=uut, attributes=['info[(.*)][bandwidth]'])
interface_before.learn()

```

Now in a seperate terminal ssh into your device

If the lab you are using is the Sandbox - ssh cisco@10.10.20.48   password cisco_1234!  

If the lab you are using is a local vagrant machine - ssh -p 3122 vagrant@127.0.0.1 vagrant

```bash
conf t
interface GigabitEthernet3
bandwidth 50000

```

Now enter the following code:-

```python
interface_after = Interface(device=uut, attributes=['info[(.*)][bandwidth]')
interface_after.learn()

```

And finally compare the two by entering the following code:-

```python
diff = interface_after.diff(interface_before)
print(diff)

```

---

**Conclusion**

As demonstrated the Ops library is an extremely useful set of tools for retrieving state data from your devices.  The
preceding exercise only explored the Ops _Model_ for IOSXE Interfaces.  There are hundreds of further models at your disposal
that support a vast range of features across IOSXE, IOSXR and NXOS.  To view the available models please go to [Model Wiki](https://pubhub.devnetcloud.com/media/pyats-packages/docs/genie/genie_libs/#/models)

**Full Script**

```python

import pprint
from genie.conf import Genie

from genie.libs.ops.interface.iosxe.interface import Interface

testbed = Genie.init('vagrant_single_ios.yaml')

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