import subprocess
import re

# Run tshark command and capture the output
tshark_command = [
    'tshark', '-r', 'new.pcapng', '-Y', 'dns.qry.name', '-T', 'fields', '-e', 'dns.qry.name'
]
process = subprocess.Popen(tshark_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# Initialize a list to hold hex parts
hex_parts = []

# Process each line of tshark output
for line in stdout.decode().splitlines():
    # Extract the hex part before ".akasec.ma"
    match = re.match(r'([0-9a-f]+)\.akasec\.ma', line)
    if match:
        hex_part = match.group(1)
        hex_parts.append(hex_part)

# Concatenate all hex parts
concatenated_hex = ''.join(hex_parts)

print(concatenated_hex)
