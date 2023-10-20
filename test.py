#!/usr/bin/env python3

import json
from f5.bigip import ManagementRoot
import icontrol.exceptions

# Define unique variables
user = 'arnob'
password = 'P$64sNI$t'
f5_ip = '10.96.35.230'
partition = 'INH-UAT'

print("[DEBUG] Connecting to F5 BIG-IP...")

# Connect to the F5
mgmt = ManagementRoot(f5_ip, user, password)
ltm = mgmt.tm.ltm

print("[DEBUG] Connected to F5 BIG-IP.")

# Initialize the data structure
data = []

# Fetch virtual servers
print("[DEBUG] Fetching virtual servers...")
virtuals = ltm.virtuals.get_collection()

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

    # Fetch associated pool members
    if virtual.pool:
        print(f"[DEBUG] Fetching pool members for virtual server: {virtual.name}")
        try:
            pool = ltm.pools.pool.load(name=virtual.pool.split('/')[-1], partition=partition)
            for member in pool.members_s.get_collection():
                vs_data["pool_members"].append({
                    "ip": member.address,
                    "port": member.name.split(':')[-1]
                })
        except icontrol.exceptions.iControlUnexpectedHTTPError as e:
            if "was not found" in str(e):
                print(f"[WARNING] Pool {virtual.pool.split('/')[-1]} in partition {partition} not found.")
            else:
                raise  # re-raise the exception if it's not a "not found" error

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
