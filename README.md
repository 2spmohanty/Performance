# Operation Performance

This framework provides a concurrent framework to do vCenter specific Operation. Not only it completes the operation but also it plots resource usage of vCenter Host objects involved in Operation.

The resource usage provides useful stats which can be beneficial data, which can be utilized to determine the ideal number of concurrent operation for a specific task.

For example the below image displays the result of 16 VM Concurrent Cloning Operation.

![16 VM Concurrent Cloning Operation](https://raw.githubusercontent.com/2spmohanty/Performance/master/images/16_16_Ops.png)

The below image depicts the resource usage aswell as time taken if the Operation would have proceeded sequentially.

![16 VM Sequential Concurrent Operation](https://raw.githubusercontent.com/2spmohanty/Performance/master/image/16_1_Ops.png)
 
# How to Run.

An Input text file needs to be created in the following formatt. 
The format is :

OPSName-Instance-PARAMETER=VALUE

The * in instance value indicates that it is applicable to all instance.

```
CloneOps-*-PRIMARY_LDU_NAME=52.32.13.1
CloneOps-*-PRIMARY_LDU_USER_NAME=administrator@vsphere.local
CloneOps-*-PRIMARY_LDU_PASSWD=YellowMellow!



CloneOps-*-STAT_COLLLECTION_LIST=pnic,datastore

CloneOps-*-DATACENTER=Datacenter3


CloneOps-*-CLUSTER=cloud_cluster_3
CloneOps-*-HOST_NAME=w1-hs4-n2201.eng.vmware.com
CloneOps-*-SRC_PNIC=vmnic0


CloneOps-*-DEST_CLUSTER=cloud_cluster_4
CloneOps-*-DEST_HOST_NAME=w1-hs4-n2206.eng.vmware.com
CloneOps-*-PNIC=vmnic0

CloneOps-1-SRC_VM_NAME=Test-VM-17
CloneOps-1-VM_NAME=Test-VM-33
CloneOps-1-DATASTORE=Local-2201-2
CloneOps-1-DEST_DATASTORE=Local-2206-1

CloneOps-2-SRC_VM_NAME=Test-VM-18
CloneOps-2-VM_NAME=Test-VM-34
CloneOps-2-DATASTORE=Local-2201-2
CloneOps-2-DEST_DATASTORE=Local-2206-1
```

##Run:

```
python concurrencytrigger.py -f '/Performance/framework/data/3.txt' -o CreateVmOps -t 16 -d
```

The -f parameter indicates the input file and -t indicates the number of concurrent process.
