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
easypy vxlancheckjob.py -html_logs -no_archive -testbed_file vagrant_single_ios.yaml 
```

Once completed review the report file generated

```bash
less runinfo/vxlancheckjob.xxxxxxxxxxxxxxx/vxlancheckjob.report
```

And then open up the Task.html file in the runinfo directory

```bash
open runinfo/vxlancheckjob.xxxxxxxxxxxxxxxx/TaskLog.html
```

Once you have reviewed the web page and the report enter the following commands

```bash
rm -rf runinfo
```


From your terminal ssh into your device

If the lab you are using is the Sandbox - ssh cisco@10.10.20.48   password cisco_1234!  

If the lab you are using is a local vagrant machine - ssh -p 3122 vagrant@127.0.0.1 vagrant

```bash
conf t
interface nve 1
shut
```

Exit the session from your device and rerun Easypy

```bash
easypy vxlancheckjob.py -html_logs -no_archive -testbed_file vagrant_single_ios.yaml 
```

And finally review the report and open the Task.html file

```bash
less runinfo/vxlancheckjob.xxxxxxxxxxxxxxx/vxlancheckjob.report

open runinfo/vxlancheckjob.xxxxxxxxxxxxxxxx/TaskLog.html
```


### Congratulations you have now finished the DEVWKS-2601 Workshop

[Beginning](../README.md)   [Back](./step7.md)  [Next](./step8.md)