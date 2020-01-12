# OVM-3.2.X-Python-Script-To-List-All-Running-VM-s-On-All-Dom0-Nodes-Managed-By-Oracle-VM-Manager
Python Script Attached will list all the VM's on all the Dom0 Nodes Managed by Oracle VM Manager along with their status (running/stopped) and on which OVS Dom0 node they are running.

Syntax: Below is syntax for running the Python script on Host running Oracle VM Manager 3.2.X.

        /usr/bin/ovm_shell.sh -u admin -p <password> -i /tmp/ovm-32x-list-all-running-vms.py
 
Replace password in above command will "admin" user password of Oracle VM Manager (OVMM).

====== Sample Output ==========


Below is example output of attached Python script showing the list of running VM's


      0004ZZZZZZZ00009d9cdea1e0bf51cc|Running|test-VM1|ovs-node-14
      0004ZZZZZZZ00005118cfe78d6b6365|Running|test-VM2|ovs-node-13
      0004ZZZZZZZ0000a6622dc796d893aa|Stopped|OL6-Test-VM|None
      0004ZZZZZZZ0000a4d2e1cc79b3d841|Running|test2|ovs-node-13
      0004ZZZZZZZ0000294c76c72302e72d|Running|test-VM123|ovs-node-15

