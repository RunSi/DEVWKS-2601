### Using pyATS run to initiate a Test with the new VxLAN Genie Ops model

Now that we have a newly created VxLAN Genie Ops Model we can leverage it within the pyATS framework.  

The functionality pyATS AETest is beyond the scope of this workshop, however running the commands below
will demonstrate the power of pyATS for automating and reporting on your testing protocols.

---

Run the following command in your terminal session

```bash
pyats run job vxlancheckjob.py  --testbed-file mocked_first.yaml 
```

Open up the report on the test by entering the following command

```bash
pyats logs view
```

---




## Congratulations you have now finished the DEVWKS-2601 Workshop

---


### Be sure to attend DEVWKS-2595 Stateful Network Validation using pyATS + GENIE


[Beginning](../README.md)   [Back](./step6.md)  [Next](../README.md)
