"""
Script: get_manufacturer.py
By: Martina Atkinson
Purpose: Function to get matching manufacturer for input MAC address
Prerequisites: Dictionary with key value pairs encountered in log file during testing.
Tested: 12/11/2022
"""


# create a function to get the manufacturer
def get_manufacturer(mac_value: str)->str:
    """ function to return the manufacturer based on the input MAC address """
    # create a dictionary item to hold the QUI Codes
    my_dictionary = {"BC:5F:F4": "ASRock Incorporation", "C8:4B:D6": "Dell" , "A4:4C:C8": "Dell", "C0:25:A5": "Dell", "18:68:CB" :  "Hangzhou" , "B8:27:EB" : "Rasberry PI"}
    # Truncate the mac value to get the QUI codes for each company which are 8 characters long
    if len(mac_value) > 8:
        mac_value = mac_value[0:8]
        # convert mac address form the input log to uppercase
    convert_mac_to_uppercase =  mac_value.upper()
    
    # if the mac address is in the dictionary return the value
    if convert_mac_to_uppercase in my_dictionary:
        # if found return value that matches the QUI key
        return(my_dictionary[convert_mac_to_uppercase])
    else:
        # if no matching key pair value found, return unknown
        return "unknown"