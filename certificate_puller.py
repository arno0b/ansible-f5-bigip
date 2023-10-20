#!/usr/bin/env python3

from f5.bigip import ManagementRoot
import icontrol.exceptions

# Define unique variables
user = 'arnob'
password = 'P$64sNI$t'
f5_ip = '10.96.35.230'

print("[DEBUG] Connecting to F5 BIG-IP...")

# Connect to the F5
mgmt = ManagementRoot(f5_ip, user, password)

print("[DEBUG] Connected to F5 BIG-IP.")

# Fetch SSL certificates from the specified path
print("[DEBUG] Fetching SSL certificates...")
certs = mgmt.tm.sys.file.ssl_certs.get_collection()

# Initialize the data structure for the .ini file
ini_data = "[ssl_certs]\n"

# Process each SSL certificate and add to the .ini data
for cert in certs:
    ini_data += f"{cert.fullPath}\n"

print("[DEBUG] Finished processing SSL certificates.")

# Save the .ini data to a file
with open('ssl_certs_inventory.ini', 'w') as ini_file:
    ini_file.write(ini_data)

print("[DEBUG] SSL certificates inventory saved to ssl_certs_inventory.ini.")
