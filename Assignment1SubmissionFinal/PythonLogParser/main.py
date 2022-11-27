"""
Script: main.py
By: Martina Atkinson
Purpose: Retrieves information from a network log file and writes to output .csv file (MAC address, company name and IP address)
Prerequisites: dhcpd.log (input file) 
Tested: 12/11/2022
"""
# import functions, remove_brackets & get_manufacturer, from my_library folder
import my_library

# variable to hold log file name and location
input_log_file = "./input_logs/dhcpd.log"

# variable to hold results csv filename and location
results_csv_file = "./results/nodes.csv"

# create a dictionary list to hold the addresses found for tracking any duplicates
list_of_addresses_found = []

# open the network log file for read
read_file = open(input_log_file, "r")

# open the results .csv file for write
write_file = open(results_csv_file, "w")


# reading every line in the input log file
for individual_line in read_file:

    # line remainder taking from 34th character onwards of each line, as initial part of line not relevant to project
    line_remainder = individual_line[34:] 
    # space character used to split input data into an array 
    segments = line_remainder.split(' ')
    # index postion [0] assigned to record type, to we can differentiate records in the log file
    record_type = segments[0]
    # set a variable to hold mac_address and used when a mac_address found in different record types
    mac_address = ""
    
    # set blank variable name for node name if found
    node = ""
    
    # return ip address at default index position 2 as this is most common location
    IP_address = segments[2]
    
    #check for record type uid where MAC addres is at index[5]
    if record_type == "uid":
        mac_address = segments[5]

    # check for record type DHCPOFFER with MAC address at index[4]
    if record_type ==  "DHCPOFFER":       
        mac_address = segments[4]   
        
    # check for record type DHCPPACK with MAC address at index[4]
    if record_type == "DHCPACK":
        mac_address = segments[4]
        # found second type of DHCPACK during testing e.g. DHCPACK to 192.168.5.21 (c0:25:a5:66:81:fc) via eth0
        # if mac_address has brackets remove with function remove_brackets 
        if segments[3].find("(")>-1:          
            mac_address = my_library.remove_brackets(segments[3])

    
    # check for record type DHCPDISCOVER - IP is not in default column - in column 4
    if record_type ==  "DHCPDISCOVER" :
        mac_address = segments[2]
        IP_address = segments[4]
          
    if record_type == "DHCPREQUEST":
        # mac_address in index 4 position 
        mac_address = segments[4]
        # additional check as some have mac_address in column 5
        if mac_address == "from":
            mac_address = segments[5]
        # detect presence of bracket in index 5 - if present indicates a node name
        if segments[5].find("(")>-1:
           #node = segments[5]
           node = my_library.remove_brackets(segments[5])
           
   # check for duplicate mac address, only add if not already processed
    if len(mac_address) > 0:
        # only valid addresses come in 
        if mac_address in list_of_addresses_found:
            # Check if mac_address already added - if so ignore, thereby preventing duplicates
            pass

        else:
            # add the mac_address the list of already found mac_address        
            list_of_addresses_found.append(mac_address)
            # print lines for debugging purposes
            print(list_of_addresses_found)
            # get manufactuer by calling the function get_manufacturer imported from my_library
            manufacturer = my_library.get_manufacturer(mac_address)
            # some IP characters had extra characters so had to strip them off
            stripped_IP_address = IP_address.strip()
            # write_file.write(mac_address + "," + IP_address + "," +node  + "," + manufacturer +"\n")
            write_file.write(mac_address + "," + stripped_IP_address + "," +node  + "," + manufacturer +"\n")       
# end of loop close the ouptut results file
write_file.close