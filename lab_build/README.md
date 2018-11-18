## Lab Setup

The Vagrantfile in this directory will build two CSR1000v routers running IOS XE 16.08

The CSR1000v IOSXE Boxes must be available on your system.  
Instructions for creating the CSR1000v Boxes can be found at:-  [Box Building](https://github.com/hpreston/vagrant_net_prog/tree/master/box_building)  

The two routers 'iosxe1' and 'iosxe2' will be connected together via GigabitEthernet2

### Ansible

The Vagrantfile once importing the boxes will automatically run the ansible_provision.yaml.  
The ansible playbook will configure both routers to peer with each other over BGP and redistribute loopbacks.  The ansible playbook
also configure NVE interfaces between the two routers.  Vxlan peering will be established between the two routers.