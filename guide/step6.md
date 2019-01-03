### GENIE Creating a MetaParser and an OPS object


For the next step in the exercise we are going to create a parser for 'show nve peers' as an additional parser
to 'show nve vni'.

We shall also leverage the MetaParser package in order verify that the output is in accordance with the schema
we define.

### Metaparser Package

There exists multiple ways to parse the device output, with different packages with each their style. 
There also exist multiple ways to communicate with the device (Cli, Xml, Rest, Yang, etc.) with each providing 
different structure for the same information!

Metaparser role is to unify those packages, into one location and one structure. 
A unified collection of parser, which works across multiple parser packages, and across multiple communication 
protocols and still returns a common structure. Metaparser allows to have one script which works across 
multiple OS, multiple communication protocol and parsing packages.

As we are only dealing with CLI and IOSXE we are not using the full power of the Metaparser package, but are leveraging
the schema engine.
The schema engine controls how and what the information is parsed should be structured.




[Beginning](../README.md)   [Back](./step5.md)  [Next](./step7.md)