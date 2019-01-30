### Using EasyPy to run a Test with the new VxLAN Genie Ops model

Now that we have a newly created VxLAN Genie Ops Model we can leverage it within the pyATS framework.  

The functionality of Easypy and pyATS AETest is beyond the scope of this workshop, however running the commands below
will demonstrate the power of pyATS for automating and reporting on your testing protocols.

---

Open a new terminal session and go to the scripts directory

```bash
cd ~/DEVWKS-2601/scripts

```

Now run the following command in your terminal session

```bash
easypy vxlancheckjob.py -html_logs . -no_archive -testbed_file mocked_first.yaml 
```

Open up the Task.html file in the runinfo directory

```bash
open TaskLog.html
```

---




## Congratulations you have now finished the DEVWKS-2601 Workshop

---

*Restore the laptop to it's initial state*

```bash
$ ./lab_cleanup.sh
```

### Be sure to attend DEVWKS-2595 Stateful Network Validation using pyATS + GENIE


[Beginning](../README.md)   [Back](./step6.md)  [Next](./step1.md)
