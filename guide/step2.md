### The Topology

Prior to initiating any tests then the network needs to be described in a Topology File. 


The topology file is written in yaml and will describe attributes of your test network, 
such as device type, login details, login method, links between devices etc.  

The GENIE Topology object is created by issuing the following commands:-

```python
from genie.conf import Genie

testbed = Genie.init('path_to_name_of_yaml_file')

```
The topology file for this lab is displayed below.  The topology file describes two devices _iosxe1_ and _iosxe2_.


```yaml

testbed:
    name: IOS_Testbed
    tacacs:
        username: vagrant
    passwords:
        tacacs: vagrant
        enable: vagrant

devices:
    iosxe1:
      alias: iosxe1
      type: CSR1000v    
      os: iosxe
      connections:
        ssh:
          protocol: ssh
          ip: 127.0.0.1
          port: 3122
      custom:
        abstraction:
          order: [os, type]

    iosxe2:
      alias: iosxe2
      type: CSR1000v    
      os: iosxe
      connections:
        ssh:
          protocol: ssh
          ip: 127.0.0.1
          port: 3222
      custom:
        abstraction:
          order: [os, type]


topology:
  iosxe1:
    interfaces:
      GigabitEthernet1:
        ipv4: 10.0.2.15/24
        link: management_link
        type: ethernet
      GigabitEthernet2:
        ipv4: 192.168.100.20/24
        link: iosxe1_to_iosxe2
        type: ethernet

  iosxe2:
    interfaces:
      GigabitEthernet1:
        ipv4: 10.0.2.15/24
        link: management_link
        type: ethernet
      GigabitEthernet2:
        ipv4: 192.168.100.21/24
        link: iosxe1_to_iosxe2
        type: ethernet
```

Some important points to note with the topology file.

* The testbed must have a name - in this case IOS_NXOS_Testbed
* The devices described - their name must correspond exactly with the hostname of the device in the testbed. e.g. iosxe1 is the hostname of the first device

The topology file for this lab can be found at:- [Topology](../scripts/vagrant_multi_ios.yaml)


Once the topology file has been initiated with ```Genie.init('path_to_yaml_file')``` a testbed object will be created.  
The testbed object will have a number of attributes, objects and methods, a set of these are described in the diagram below.
![topology](../images/topologyobject.png)


### Load the Genie Library and instantiate the testbed file

Change directory and run an iPython interactive shell:-

```bash
$cd scripts

$iPython
```

Import the Genie library from genie.conf and initiate the testbed file

```python
from genie.conf import Genie

testbed = Genie.init('vagrant_multi_ios.yaml')

```

The topology object that has been created is called testbed.  Now look at some of the attributes
of the topology object by issuing the following commands

```python

testbed.devices 

testbed.name 

testbed.interfaces

```

The topology file has numerous attributes, objects and methods, to view these then in the iPython session type
**testbed.** and press tab.  Alternatively you can issue the following command within iPython

```python

dir(testbed)
```

To explore further attributes and methods then enter the following within iPython (or tab completion)

```python
dir(testbed.devices)
```

You will see that from issuing this command that testbed.devices has number of attributes/objects/methods, of note are
_iosxe1_ and _iosxe2_


Once again type within iPython (or tab completion)

```python
dir(testbed.devices.iosxe1)
```
You should see are large number of attributes/objects/methods.  Of particular note is the _connect_ method.  We shall be using the 
_connect_ method to establishing connectivity with our testbed devices in forthcoming exercises.




[Beginning](../README.md)   [Back](./step1.md)  [Next](step3a.md)