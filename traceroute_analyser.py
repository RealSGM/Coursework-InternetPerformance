import os
import re

output = {}

'''
    output format
    output = {
        'file1.txt': {
            'www.harvard.edu': [
                {
                    'hop': 1,
                    'address': 'www.com',
                    'ip': '0.0.0.0',
                    'average_time': 0.0
            }
        ]
    }
'''

def process_line(line, hop):
    cleaned_lines = []
    
    # cleaned_lines = [item for item in cleaned_lines if item != 'ms'] # remove ms
    # cleaned_lines = [item for item in cleaned_lines if '*' not in item] # remove *
    # cleaned_lines = list(filter(None, cleaned_lines)) # remove empty strings
    
    # hop_dict = {}
    # hop_dict['hop'] = cleaned_lines[0]
    # hop_dict['address'] = cleaned_lines[1]
    # hop_dict['ip'] = cleaned_lines[2]
    
    return cleaned_lines

def process_log_contents(contents):
    hops = {'www.harvard.edu': [], 'www.cuhk.edu.hk': [], 'www.unimelb.edu.au': [], 'www5.usp.br': []}
    current_hop = None
    
    for line in contents.split('\n'):
        match = re.search(r'([\d]+\.[\d]+\.[\d]+\.[\d]+|\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}\b)', line)
        if match:
            hop = match.group(0)
            
            if line.startswith('traceroute'):
                current_hop = str(hop)
            else:
                # cleaned_lines = process_line(line, hop)
                
                hops[current_hop].append(line)
    return hops

def loop_through_files(folder):
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder, file), 'r') as f:
                contents = f.read()
                hops = process_log_contents(contents)
                output[file] = hops

if __name__ == '__main__':
    loop_through_files()
    
    # for file, hops in output.items():
    #     print(f'File: {file}')
    #     for address, hop in hops.items():
    #         print(f'Address: {address}')
    #         for line in hop:
    #             print(line)
    #         print('\n')
    #     print('\n\n')