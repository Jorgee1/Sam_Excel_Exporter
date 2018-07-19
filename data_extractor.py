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


def testx():
    print("Module Test")

if __name__ == "__main__":
    PTH = "data/"

    patterns = {
        'Name': 'Target:[A-Za-z\t_0-9 .]+',
        'Services': 'show service service-using | match "Matching"',
        'Saps': 'show service sap-using | match "Number"',
        'Ports': 'show port description | match 10/100/G',
    }

    format = {
        'Name':'',
        'Services':'0',
        'Saps':'0',
        'Ports':'0',
    }

    with open('data/131.txt', 'r') as file:
        data = file.read().splitlines()
        size = len(data)
        for index in range(size):
            #print(str(index)+":", data[index])

            if re.search(patterns['Name'], data[index]):
                name = re.search(patterns['Name'], data[index]).group().replace('Target:', '')
                print("Name:",name)
            elif re.search(patterns['Services'], data[index]):
                if re.search(r'Matching Services : [0-9]+', data[index+1]):
                    print('Services:', re.search(r'[0-9]+', data[index+1]).group())
                    index = index + 1
            elif re.search(patterns['Saps'], data[index]):
                print(data[index+1])
                if re.search(r'Number of SAPs : [0-9]+', data[index+1]):
                    print('Saps:', re.search(r'[0-9]+', data[index+1]).group())
                    index = index + 1

        """
        for line in data:
            if re.search(patterns['Name'], line):
                name = re.search(patterns['Name'], line).group().replace('Target:', '')
                print(name)
            elif re.search(patterns['Services'], line):
                print(data.readline())
            elif re.search(patterns['Saps'], line):
                print(data.readline())
            elif re.search(patterns['Ports'], line)
                print(data.readline())

        """
        """
            for key, pattern in patterns.items():

                if key == 'Name':
                    if re.search(pattern, i):
                        print('Name:', re.search(pattern, i).group().replace('Target:', ''))
                        cosa['Name'] = re.search(pattern, i).group().replace('Target:', '')
                elif key == 'Saps':
                    if re.search(pattern, i):
                        print('Saps', re.search(r'[0-9]+', i).group())
                        cosa['Saps'] = re.search(r'[0-9]+', i).group()
                elif key == 'Services':
                    if re.search(pattern, i):
                        print('Services:', re.search(r'[0-9]+', i).group())
                        cosa['Services'] = re.search(r'[0-9]+', i).group()
                elif key == 'Ports':
                    if re.search(pattern, i):
                        count = 0
                        while f:
                            temp = f.readline()
                            if len(temp)>4:
                                count = count +1
                            else:
                                break;
                        print("Ports:", count)
                        cosa['Ports'] = count
                        #print("------------------------------")
                        flag = True

                if flag:
                    data.append(cosa)
                    flag = False
                    print(cosa)
                    cosa = {
                        'Name':'',
                        'Services':'0',
                        'Saps':'0',
                        'Ports':'0',
                    }
            """
