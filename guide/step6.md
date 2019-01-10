### GENIE Creating an OPS object

We are now going to create a VxLAN OPS object that will collate the output of the two parsers we created earlier.

For the sake of brevity these two parsers have been defined within Classes in the file [iosxevxlan.py](../scripts/iosxevxlan.py).  
The parsers are also inheriting from Genie Metaparser.  The configuration of Metaparser is outside the scope of this workshop
but further details can be found at - [Metaparser](https://pubhub.devnetcloud.com/media/pyats-packages/docs/metaparser/index.html)

---

If you have an iPython session running. Close and restart iPython

Initiate an iPython interactive session and intialise the testbed

```bash

$ ipython

import pprint
from genie.conf import Genie
testbed = Genie.init('vagrant_single_ios.yaml')
uut = testbed.devices.iosxe1
uut.connect()

```    


First we shall import from Genie ops the Base class.  We will create a class that will inherit from 'Base' to leverage the
'Maker' functionality.  
'Maker' simplifies the process of mapping parsers output to the ops object attributes. 

Further information on the Maker class can be found at [Maker](https://pubhub.devnetcloud.com/media/pyats-packages/docs/genie/Ops/developer/maker.html) 

In addition we will import the parsers that were created earlier.

Enter the code below into your ipython session

```python
from genie.ops.base import Base
from iosxevxlan import ShowNveVni,ShowNvePeers

```

We now create a class that will be our Ops object, named Vxlan.  This class inherits from the Base class of Genie Ops.  
A method which referred to as _learn_ is created.  The remaining code performs the following functions  

* Runs a for loop issuing the commands for the parsers and then adds data (add_leaf) to the new Ops object structure.
* src is the dictionary item from the parsed output. For example '['(?P<interf>.*)][VNI]' will equate to the value of VNI (6001)
* dest is where the data will be placed in the new object structure referenced as *info*.  In this case the src and dest keys are the same
but this does not have to be the case
* Finally the make() is invoked to finalise the new object structure.

```python
class Vxlan(Base):

    def learn(self, custom=None):


        # Capture output from ShowNveVni parser
        src = '[(?P<interf>.*)]'
        dest = 'info[(?P<interf>.*)]'
        req_keys = ['[VNI]','[Multicast-group]','[VNIstate]','[Mode]']
        for key in req_keys:
            self.add_leaf(cmd=ShowNveVni,
                          src=src + '[{}]'.format(key),
                          dest=dest + '[{}]'.format(key))


        # Capture ouptut from ShowNveVni parser
        src = '[(?P<nvename>.*)]'
        dest = 'info[(?P<nvename>.*)]'
        req_keys = ['[Peer-IP]','[Router-RMAC]','[Type]','[state]']
        for key in req_keys:
            self.add_leaf(cmd=ShowNvePeers,
                          src=src + '[{}]'.format(key),
                          dest=dest + '[{}]'.format(key))

        #Add ops data to the Vxlan ojbect
        self.make()
```

Finally create a new ops object called myvxlan and learn from the device

```python
myvxlan = Vxlan(device=uut)

myvxlan.learn()

myvxlan.info

```

Disconnect from the device
```python
uut.disconnect()
```

### You have successfully created a VxLAN Ops Model.




[Beginning](../README.md)   [Back](./step5.md)  [Next](./step7.md)