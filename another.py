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

# Initialize the data structure
data = []

# Fetch virtual servers
virtuals = ltm.virtuals.get_collection()

for virtual in virtuals:
    vs_data = {
        "name": virtual.name,
        "port": virtual.destination.split(':')[-1],  # Extract port from the destination
        "pool_members": [],
        "clientssl_profile": [],
        "serverssl_profile": [],
        "snatpool": virtual.sourceAddressTranslation.get('pool', None),
        "vlan": virtual.vlans if hasattr(virtual, 'vlans') else None,
        "http_profile": []
    }

    # Fetch associated pool members
    if virtual.pool:
        pool = ltm.pools.pool.load(name=virtual.pool.split('/')[-1], partition=partition)
        for member in pool.members_s.get_collection():
            vs_data["pool_members"].append({
                "ip": member.address,
                "port": member.name.split(':')[-1]
            })

    # Fetch profiles associated with the virtual server
    for profile in virtual.profiles_s.get_collection():
        if profile.context == 'clientside' and 'clientssl' in profile.name:
            vs_data["clientssl_profile"].append(profile.name)
        elif profile.context == 'serverside' and 'serverssl' in profile.name:
            vs_data["serverssl_profile"].append(profile.name)
        elif 'http' in profile.name:
            vs_data["http_profile"].append(profile.name)

    data.append(vs_data)

# Print the data in JSON format
print(json.dumps(data, indent=4))
