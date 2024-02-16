import yaml

def extract_details_corrected(line):
    """
    Correctly extracts details from a line of the input file, handling missing elements gracefully.
    """
    details = {
        'trusted_cert_authority': '',
        'cert': '',
        'chain': '',
        'key': '',
        'peer-cert-mode': '',
        'renegotiation': ''
    }
    
    try:
        details['trusted_cert_authority'] = line.split('ca-file ')[1].split(' ')[0].strip()
    except IndexError:
        details['trusted_cert_authority'] = ''

    try:
        cert_key_chain_part = line.split('cert-key-chain')[1].split('}')[0]
        for part in cert_key_chain_part.split('\n'):
            if 'cert ' in part:
                details['cert'] = part.split('/Common/')[1].split(' ')[0]
            elif 'chain ' in part:
                details['chain'] = part.split('/Common/')[1].split(' ')[0]
            elif 'key ' in part:
                details['key'] = part.split('/Common/')[1].split(' ')[0]
    except IndexError:
        details['cert'] = details['chain'] = details['key'] = ''

    try:
        details['peer-cert-mode'] = line.split('peer-cert-mode ')[1].split(' ')[0].strip()
    except IndexError:
        details['peer-cert-mode'] = ''

    try:
        details['renegotiation'] = line.split('renegotiation ')[1].split(' ')[0].strip()
    except IndexError:
        details['renegotiation'] = ''
    
    return details

def reformat_content_with_corrected_extraction(file_content):
    lines = file_content.split('\n')
    reformatted_lines = []

    for line in lines:
        if line.startswith('ltm profile client-ssl'):
            name = line.split(' ')[3]
            details = extract_details_corrected(line)

            reformatted_line = (
                f"-name: {name}\n"
                f" trusted_cert_authority: {details['trusted_cert_authority']}\n"
                f" cert: /Common/{details['cert']}\n"
                f" chain: /Common/{details['chain']}\n"
                f" key: /Common/{details['key']}\n"
                f" peer-cert-mode: {details['peer-cert-mode']}\n"
                f" renegotiation: {details['renegotiation']}"
            )
            reformatted_lines.append(reformatted_line)

    return '\n\n'.join(reformatted_lines)

# To use this code, you would read the file content as follows:
file_path = r'C:\Users\saadman.arnob\Downloads\Gitea\UAT_Playbooks\Fintech_DR_Config\SSL Profile Creation Playbooks\clientssl_inven.txt'  # Change this to the path of your file

with open(file_path, 'r') as file:
    file_content = file.read()

# Apply the reformatting function to the file content
reformatted_content = reformat_content_with_corrected_extraction(file_content)

print(reformatted_content)



