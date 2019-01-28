# Getting Started

In order to follow this lab please clone the DEVWKS-2601 repository from github

```bash

$ cd workspace/DEVWKS-2601/DEVWKS-2601/

$ source ./lab_setup.sh
```

### Lab_script

Your development environment will be setup by 'sourcing' lab_script.sh  
The script performs the following actions:-

* Sets up a local python3 virtual environment and installs all necessary
 dependencies.  
* Brings up a CSR1000v using Vagrant  
* Configures the CSR1000v for:-  
    * Netconf
    * Interface configuration
    * Loopback configuration
    * Creates BGP Configuration
    * Creaets VxLAN configuration
    
Please allow several minutes for the script to complete

[Beginning](../README.md)   [Back](../README.md)  [Next](./step2.md)

