import pandas as pd

ip_addresses = {
    "www.fmprc.gov.cn": [], 
    "www.gov.scot": [], 
    "www.gov.za": [], 
    "www5.usp.br": []
}

# read the csv file
def load_csv(path):
    return pd.read_csv(path)

# main function
def main(path):
    traceroute_results = load_csv(path)
    
    ## Loop through each row in the traceroute_results
    ## Calculate the average time for each ip address to respond
    
    for (file, address), group in traceroute_results.groupby(['File', 'Address']):
        # Loop through the rows in the group
        temp_time = 0
        for i, row in group.iterrows():
            temp_time += row['Average Time']
        ip_addresses[address].append(temp_time)
    
    for address, times in ip_addresses.items():
        # Calculate hte average in times
        average_time = round(sum(times) / len(times),2)
        ## Round time to 2 decimal places
        print(f'{address} average time: {average_time}ms')
    

main('TraceRouteCode/traceroute.csv')