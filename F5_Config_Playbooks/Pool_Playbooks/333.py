import re
from collections import defaultdict
import yaml

def read_inventory_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def is_ip_address(node_name):
    # Updated regular expression to accurately match IP addresses
    return re.match(r'^\d{1,3}(\.\d{1,3}){3}$', node_name)

def refine_member_details(members_block):
    refined_members = []
    members_details = members_block.split('}')

    for member_detail in members_details:
        if member_detail.strip():
            # Initialize variables to store FQDN and IP address
            fqdn_name, ip_address = None, None

            # Attempt to capture FQDN name
            fqdn_match = re.search(r'fqdn\s*\{\s*autopopulate\s+enabled\s+name\s+([\w\.-]+)', member_detail)
            if fqdn_match:
                fqdn_name = fqdn_match.group(1)

            # Attempt to capture direct IP address
            ip_match = re.search(r'address\s+([\d\.]+)', member_detail)
            if ip_match:
                ip_address = ip_match.group(1)

            # Check for 'state fqdn-up'
            fqdn_up = 'state fqdn-up' in member_detail
            
            # Determine address priority: Direct IP if available, otherwise FQDN name
            address = ip_address if ip_address else fqdn_name

            # Further processing to extract node_name, protocol, etc., as before
            node_protocol_port_match = re.search(r'([\w\/\._-]+):([\w-]+)?(?:\:(\d+))?', member_detail)
            if node_protocol_port_match:
                node_name, protocol, port = node_protocol_port_match.groups()
                # Skip if node_name is an IP address
                if is_ip_address(node_name.split('/')[-1]):
                    continue
                
                refined_members.append({
                    'node_name': node_name,
                    'protocol': protocol or "Not specified",
                    'port': port or "Not specified",
                    'address': address,
                    'fqdn_up': fqdn_up,
                    'autopopulate_enabled': fqdn_match is not None,
                })

    return refined_members

def process_inventory(pool_inventory_contents):
    pool_pattern = re.compile(r'ltm pool ([\w-]+) { members { ([\s\S]+?) } (?:monitor ([\S\s]+?)\s)?partition ([\w]+)')
    inventory_list = []

    for match in pool_pattern.findall(pool_inventory_contents):
        pool_name, members_block, monitor, partition = match
        refined_members = refine_member_details(members_block)
        
        for member in refined_members:
            inventory_item = member.copy()
            inventory_item.update({
                'pool_name': pool_name,
                'monitor': monitor.strip() if monitor and monitor.strip() != 'monitor' else 'Not specified',
                'partition': partition
            })
            inventory_list.append(inventory_item)

    return inventory_list

def save_to_yaml(inventory_list, file_path):
    with open(file_path, 'w') as yaml_file:
        yaml.dump(inventory_list, yaml_file, allow_unicode=True, default_flow_style=False)

def main():
    file_path = r'C:/Users/saadman.arnob/Downloads/Gitea/UAT_Playbooks/Fintech_DR_Config/Pool Creation Playbooks/pool_inventory.txt'  # Updated to use a relative path for the input file
    pool_inventory_contents = read_inventory_content(file_path)
    inventory_list = process_inventory(pool_inventory_contents)
    precise_yaml_file_path = r'C:/Users/saadman.arnob/Downloads/Gitea/UAT_Playbooks/Fintech_DR_Config/Pool Creation Playbooks/preci.yaml'  # Updated to a relative path for the output file
    save_to_yaml(inventory_list, precise_yaml_file_path)
    print(f'Refined inventory saved to {precise_yaml_file_path}')

if __name__ == "__main__":
    main()