# Getting Started

In order to follow this lab please clone the DevNet2601 repository from github

```bash
$ git clone https://github.com/RunSi/DevNet2601.git

$ cd DevNet2601

$ source lab_script.sh
```

### Lab_script

Your development environment will be setup by 'sourcing' lab_script.sh  
The script performs the following actions:-

* Sets up a local python3 virtual environment and installs all necessary
 dependencies.  
* Brings up two CSR1000vs using Vagrant  
* Configures the CSR1000vs for:-  
    * Netconf
    * Interface configuration
    * Loopback configuration
    * BGP Peering between the two routers
    * VXLAN session between the two routers
    
Please allow several minutes for the script to complete

[Beginning](../README.md)   [Back](../README.md)  [Next](./step2.md)

