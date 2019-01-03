### Genie Ops continued

**Partial retrieval of Ops data**

Rather than retrieving the entire state you can choose to only save the attributes you require for the interface.  
For example we only wish to retrieve the Mac Addresses of the interfaces.  To achieve this

```python
interface = Interface(device=uut, attributes=['info[(.*)][mac_address]'])
```

Now 'relearn' the interface object and display the output

```python
interface.learn

pprint.pprint(interface.info)

```

Now try and find other parameters from the interface object to learn and display (for example, 'mtu', 'bandwidth')


[Beginning](../README.md)   [Back](./step3a.md)  [Next](./step4.md)