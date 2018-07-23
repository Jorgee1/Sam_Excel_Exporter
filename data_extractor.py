import os
import re
import json
import csv

"""


Referencias

"Target:


SAP_CMD

show service service-using | match "Matching"
Matching Services : 80

show service sap-using | match "Number"
Number of SAPs : 80

show port description | match 10/100/G -> loop
1/1/4          10/100/Gig Ethernet SFP
1/1/4          10/100/Gig Ethernet SFP
1/1/4          10/100/Gig Ethernet SFP
...


"""

def extract(file_path):
    patterns = {
        'Name': 'Target:[A-Za-z\t_0-9 .]+',
        'Services': 'show service service-using | match "Matching"',
        'Saps': 'show service sap-using | match "Number"',
        'Ports': 'show port description | match 10/100/G',
    }
    #print(file_path)
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
        size = len(data)

        out = []
        temp = []
        for index in range(size):
            #print(str(index)+":", data[index])
            if re.search(patterns['Name'], data[index]):
                name = re.search(patterns['Name'], data[index]).group().replace('Target:', '')
                #print("Name:",name)
                temp.append(name)
            elif re.search(patterns['Services'], data[index]):
                if re.search(r'Matching Services : [0-9]+', data[index+1]):
                    num = re.search(r'[0-9]+', data[index+1]).group()
                    #print('Services:', num)
                    index = index + 1
                    temp.append(num)
                else:
                    temp.append(0)
            elif re.search(patterns['Saps'], data[index]):
                #print(data[index+1])
                if re.search(r'Number of SAPs : [0-9]+', data[index+1]):
                    num = re.search(r'[0-9]+', data[index+1]).group()
                    #print('Saps:', num)
                    index = index + 1
                    temp.append(num)
                else:
                    #print('Saps: 0')
                    temp.append(0)
            elif re.search(patterns['Ports'], data[index]):
                sw = True
                acc = 0
                j=1
                while sw:
                    if index+j < size and len(data[index+j])>4:
                        #print(data[index+j])
                        acc = acc + 1
                    else:
                        sw = False
                    j = j+1
                #print("Ports:", acc)
                temp.append(acc)
                out.append(temp)
                #print(temp)
                temp = []
                #print("---------------------------")
        #print(out)
        return out


if __name__ == "__main__":

    extract('data/131.txt')
