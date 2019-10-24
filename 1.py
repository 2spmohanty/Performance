from collections import OrderedDict, namedtuple, defaultdict
import glob
instance_data = {}
instance_dict= {'1': ',PRIMARY_LDU_NAME:10.172.109.23,PRIMARY_LDU_USER_NAME:administrator@skyscraper.local,PRIMARY_LDU_PASSWD:vc_password,DATACENTER:Datacenter3,CLUSTER:cls,HOST_NAME:w1-hs4-n2203.eng.vmware.com,SRC_PNIC:vmnic1,DATASTORE:vsanDatastore,SRC_DISK:vmhba2,DEST_DATACENTER:Datacenter3,DEST_CLUSTER:cls,DEST_HOST_NAME:w1-hs4-n2204.eng.vmware.com,PNIC:vmnic1,DEST_DATASTORE:vsanDatastore,DEST_DISK:vmhba2,STAT_COLLLECTION_LIST:pnic,datastore,mem,disk'}
"""
for instance in instance_dict:
    print instance
    instance_data[instance] = dict( (x, y) for x, y in (item.split(":") for item in instance_dict[instance].strip(",").split(",")))



instance = '1'
for x,y in (item.split(":") for item in instance_dict[instance].strip(",").split(",")):
    

"""

z = dict(1,2)

