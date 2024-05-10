import os
import re
# Set the directory where the files are located
directory = 'C:\\Users\\nicky\\Desktop\\Downloads\\CS2107_assignment2_dist\\2Medium\\m1_exfiltrator64'
def extract_number(filename):
    match = re.search(r'\((\d+)\)$', filename)
    if match:
        return int(match.group(1))
    else:
        return 0
# Initialize an empty list to store the combined content
payload_content = []
filenames = sorted(os.listdir(directory), key=extract_number)
#print(filenames)
# Loop through the files in the directory
for filename in filenames:
    if filename.startswith('payload'):
        # Open the file and read its contents
        with open(os.path.join(directory, filename), 'r') as file:
            content = file.read().strip()
        # Check if the content contains "req="
        if 'req=' in content:
            # Extract the text after "req="
            req_content = content.split('req=')[1]
            req_content = req_content.split('&id=')[0]
            payload_content.append(req_content)

# Join the combined content into a single string
final_content = ''.join(payload_content).strip()
#for filename in payload_content.keys():
#    final_content += payload_content[filename]

# Print the final content
#print(final_content)

with open(directory + '\\combined.txt', 'w') as file:
    file.write(final_content)
