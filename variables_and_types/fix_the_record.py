# fix_the_record.py

# This program prints a short record about a network device.



device_name = "edge-router"

#syntax error
#the name of varible strat with number
nd_ip = "192.0.2.1" 

#syntax error
#the name of varible is the Keywords (class)
class_the_device = "router" 

#runtime error
#you can not Convert  text string "twenty-two" to int 
port = int("22")

#runtime error
#the name of varible device_nam it not found in the program
print("Device:", device_name)

#synatx error

print("Backup IP:", nd_ip)

print("Type:", class_the_device)

print("Port:", port)


#Which bugs does Python report first? Explain why in a comment

#the syntax error first because it checks and parses the entire file for syntax rules before running any code 
#Runtime errors only happen later during program execution when a specific line is reached.
