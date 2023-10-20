#!/usr/bin/env python3

import json
from f5.bigip import ManagementRoot
import icontrol.exceptions

# Define unique variables
user = 'arnob'
password = 'P$64sNI$t'
f5_ip = '10.96.35.230'
partition = 'UAT'

print("[DEBUG] Connecting to F5 BIG-IP...")

# Connect to the F5
mgmt = ManagementRoot(f5_ip, user, password)
ltm = mgmt.tm.ltm

print("[DEBUG] Connected to F5 BIG-IP.")

# Initialize the data structure
data = []

# Fetch virtual servers and filter by 'INH-UAT' partition
print("[DEBUG] Fetching virtual servers from partition:", partition)
virtuals = [vs for vs in ltm.virtuals.get_collection() if vs.partition == partition]

for virtual in virtuals:
    print(f"[DEBUG] Processing virtual server: {virtual.name}")

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

    # Fetch associated pool members across all partitions
    if hasattr(virtual, 'pool') and virtual.pool:
        pool_name = virtual.pool.split('/')[-1]
        print(f"[DEBUG] Searching for pool {pool_name} across all partitions...")

        partitions = mgmt.tm.auth.partitions.get_collection()
        for part in partitions:
            try:
                pool = ltm.pools.pool.load(name=pool_name, partition=part.name)
                print(f"[DEBUG] Found pool {pool_name} in partition {part.name}.")

                # Fetch pool members' IP and port
                members = pool.members_s.get_collection()
                for member in members:
                    vs_data["pool_members"].append({
                        "ip": member.address,
                        "port": member.name.split(':')[-1]
                    })
                break
            except icontrol.exceptions.iControlUnexpectedHTTPError:
                continue

    # Fetch profiles associated with the virtual server
    print(f"[DEBUG] Fetching profiles for virtual server: {virtual.name}")
    for profile in virtual.profiles_s.get_collection():
        if profile.context == 'clientside' and 'clientssl' in profile.name:
            vs_data["clientssl_profile"].append(profile.name)
        elif profile.context == 'serverside' and 'serverssl' in profile.name:
            vs_data["serverssl_profile"].append(profile.name)
        elif 'http' in profile.name:
            vs_data["http_profile"].append(profile.name)

    data.append(vs_data)

print("[DEBUG] Finished processing virtual servers.")

# Print the data in JSON format
print(json.dumps(data, indent=4))

# Save the data to a .json file
with open('virtual_servers_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("[DEBUG] Data saved to virtual_servers_data.json.")
