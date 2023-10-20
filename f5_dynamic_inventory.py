#!/usr/bin/env python3

import json
from f5.bigip import ManagementRoot

# Define unique variables
user = 'arnob'
password = 'N@98sDS@t'
f5_ip = '10.96.35.200'
partition = 'CPS_UAT'

# Connect to the F5
mgmt = ManagementRoot(f5_ip, user, password)
ltm = mgmt.tm.ltm

# Fetch nodes
nodes = [node.name for node in ltm.nodes.get_collection()]

# Fetch pools
pools = [pool.name for pool in ltm.pools.get_collection()]

# Fetch virtual servers
virtuals = [virtual.name for virtual in ltm.virtuals.get_collection()]

# Fetch VLANs
vlans = [vlan.name for vlan in mgmt.tm.net.vlans.get_collection()]

# Fetch SSL certificates
certs = [cert.name for cert in mgmt.tm.sys.file.ssl_certs.get_collection()]

# Format the data for Ansible
inventory = {
    "f5_nodes": {
        "hosts": nodes
    },
    "f5_pools": {
        "hosts": pools
    },
    "f5_virtuals": {
        "hosts": virtuals
    },
    "f5_vlans": {
        "hosts": vlans
    },
    "f5_certs": {
        "hosts": certs
    },
    "_meta": {
        "hostvars": {}
    }
}

# Print the inventory in JSON format
print(json.dumps(inventory, indent=4))
