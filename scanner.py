#! /usr/bin/python

#This code is open-source.
# This scripts should be run on root terminal
# Before running this code, first install python3 nmap module using below command
# pip install python3-nmap

print("************************************************************************\ ") 
print("@@@@@@@@@@@@@@@@@@@@ copyright of Mr_Cyber 2023 @@@@@@@@@@@@@@@@@@@@@@@@/") 
print("************************************************************************\ ") 
print("************************************************************************/") 
print(" _         _    ___         ______           ______     ______    ___")
print("| \       / | |     \     /         \     / |       \  |        |      \ ")
print("|  \     /  | |  D   )   /           \   /  |   D    | |        |   O   )")
print("|   \ _ /   | |     /   /             \ /   | _____ /  |______  |      /")
print("|     O     | |    / __ \              |    |       \  |        |     /")
print("|    ___    | |  _ \     \             |    |   D    | |        |  __ \ ")
print("| _ |   | _ | |_| |_\     \ ______     |    | ______ / |______  |_|  |_\ ")
print("************************************************************************")
print("@@@@@@@@@@@@@ github link = https://github.com/Mr-cyber200 @@@@@@@@@@@@@") 
print("LinkendIn link = https://www.linkedin.com/in/nwarienne-michael-378b5a183") 
print("************************************************************************") 

print("Wecome!, This is nmap auto scanner by Mr_Cyber.")
print("\n")

import nmap #import nmap module

scanner = nmap.PortScanner()
#input Your IP address
while True:
    ip_address = input("Enter the IP address you want to Scan: \n")
    

#confirm your IP address and continue with the can
print("Is this the IP address you want to scan:", ip_address) 
answer = str 
while answer not in ["Yes", "yes", "Y", "y", "No", "no", "N", "n"]: 
    answer = input("Confirm your IP address: Yes or No\n") 
    if answer=="Yes" or answer=="yes" or answer=="Y" or answer=="y": 
        print("Proceed with your scan\n") 
    elif answer=="No" or answer=="no" or answer=="N" or answer=="n": 
        print("Re-input your IP address\n")
        quit() 
    else: 
        print("Please type Yes or No\n")
type(ip_address)

#Make choice of your Scan
Choice_of_scan = int(input("""Enter the type of scan you want to perform
                          
                          1. SYN SCAN
                          2. UDP SCAN
                          3. XMAX SCAN
                          4. FIN SCAN
                          5. NULL SCAN
                          6. COMPREHENSIVE SCAN: \n"""))

print("You have selected option: ", Choice_of_scan)
# To know the port status of scanned IP address
if Choice_of_scan == 1:
    print("Nmap version:", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -T4 -sS')
    print("Ip Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['tcp'].keys())
elif Choice_of_scan == 2:
    print("Nmap version:", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -T4 -sU')
    print("Ip Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['udp'].keys())
elif Choice_of_scan == 3:
    print("Nmap version:", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -T4 -sX')
    print("Ip Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['tcp'].keys())
elif Choice_of_scan == 4:
    print("Nmap version:", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -T4 -sF')
    print("Ip Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['tcp'].keys())
elif Choice_of_scan == 5:
    print("Nmap version:", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -T4 -sN')
    print("Ip Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['tcp'].keys())
elif Choice_of_scan == 6:
    print("Nmap version:", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -T4 -sS -sV -sC -A -O')
    print("Ip Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['tcp'].keys())
    print("service:", "version", scanner[ip_address].service)
elif Choice_of_scan >=7:
    print("Please enter a valid option")
else:
    quit()



