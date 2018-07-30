import os
import re
import json
import csv

""" Descripción
    Modulo para optener los datos de los documentos de texto.
    Se encarga de extraer el nombre, numero de servicios, numero de SAPs y numero de puertos de cada 7210
    Recibe un .txt y regresa un array de datos listo para guardar en un .csv
"""

def extract(file_path):

    # Diccionario de patrones asociados a un Keyword de las columnas del CSV final.
    patterns = {
        'Name': 'Target:[A-Za-z\t_0-9 .]+',
        'Services': 'show service service-using | match "Matching"',
        'Saps': 'show service sap-using | match "Number"',
        'Ports': 'show port description | match 10/100/G',
    }

    # Diccionario donde se van a ir rotando los datos de cada 7210 para a agregarlos ala variable "out" mas adelante.
    temp_data = {
        'Name':"",
        'Services':0,
        'Saps':0,
        'Ports':0,
    }

    # Lista de Keywords con el orden en el que deben aparecer en el .csv
    keys = ['Name', 'Services', 'Saps', 'Ports']

    # Se habre el archivo .csv para extraer los datos
    with open(file_path, 'r') as file:
        # Se separa en lineas el archivo y se guarda en memoria en forma de lista para hacer más facil el indexado
        # Esto es nesesario porque hay que incrementar y disminuir el indice aparte del ciclo principalself.
        # la forma normal de leer el archivo ( for line in file: ) no ofrece suficiente libertad para hacer esto.
        data = file.read().splitlines()
        size = len(data)

        # Inizialisacion de la variable que se va a regresar al final del proceso
        out = []

        # Inicio de la lectura del archivo
        for index in range(size):

            # Condicional para el caso en el que se encuentre el nombre del 7210
            # Se busca encontrar el patron 'Target:[Cualquier numero de caracteres]'
            if re.search(patterns['Name'], data[index]):
                name = re.search(patterns['Name'], data[index]).group().replace('Target:', '')
                # Se guarda el nombre en la variable antes de agregarlo a 'out'
                temp_data['Name'] = name
            # Condicional para cuando se enceuntra el numero de servicios
            # Se busca encontrar el comando 'show service service-using | match "Matching"'
            # y leer el valor de la siguiente linea
            elif re.search(patterns['Services'], data[index]):
                # Si no hay servicios asociados no muestra el patron 'Matching Services : [0-9]+' en la siguiente linea 'index+1'
                # por lo que se debe dejar el valor por defecto
                # luego de encontrar el comando se busca en la line siguiente para extraer el numero
                # Si no hay servicios relacionados el comando no muetra nada
                if re.search(r'Matching Services : [0-9]+', data[index+1]):
                    # Se extrae el numero de la linea identificada
                    num = re.search(r'[0-9]+', data[index+1]).group()
                    # se incrementa el index porque ya se revisó esa linea
                    index = index + 1
                    # Se guarda el nombre en la variable antes de agregarlo a 'out'
                    temp_data['Services'] = num
            # Condicional para cuando se encuentra el numero de SAPs
            # Se busca encontrar el comando 'show service sap-using | match "Number"'
            # y leer el valor de la siguiente linea
            elif re.search(patterns['Saps'], data[index]):
                # Si no hay servicios asociados no muestra el patron 'Number of SAPs : [0-9]+' en la siguiente linea 'index+1'
                # por lo que se debe dejar el valor por defecto
                # luego de encontrar el comando se busca en la line siguiente para extrar el numero
                # Si no hay SAPs relacionados el comando no muetra nada
                if re.search(r'Number of SAPs : [0-9]+', data[index+1]):
                    # Se extrae el numero de la linea identificada
                    num = re.search(r'[0-9]+', data[index+1]).group()
                    # se incrementa el indexporque y a se revisó
                    index = index + 1
                    # Se guarda en la variables adntes de agregarlo a 'out'
                    temp_data['Saps'] = num
            # Condicional para el conteo de puertos
            # se encuentra primero el comando 'show port description | match 10/100/G'
            # y despues se empiesa a hacer el conteo de lineas hasta que encuentre un espacio menor de 4 caracteres
            elif re.search(patterns['Ports'], data[index]):
                # Variable que guardará el numero de puertos
                acc = 0
                # variables de control del ciclo while
                sw = True
                j=1

                # se realiza el conteo de puertos
                while sw:
                    if index+j < size and len(data[index+j])>4:
                        acc = acc + 1
                    else:
                        sw = False
                    j = j+1

                # Se guarda el valor obtenido
                temp_data['Ports'] = acc

                # se adapta al formato .csv en la variable out
                temp = [temp_data[i] for i in keys]
                out.append(temp)

                # Se carga la variabel temporal con los valores por defecto
                temp_data = {
                    'Name':"",
                    'Services':0,
                    'Saps':0,
                    'Ports':0,
                }

        return out


if __name__ == "__main__":

    extract('data/131.txt')




""" Requerimientos

    Formato que debe tener el archivo para ser valido:

    #
    #Script Name:SERVICIOS_Y_SAP_CUC-VVC	Script Version:3	Target:CUC_CNT_7210_01
    #Status:Successful	Date:2018/07/16 09:30:38 821
    #Saved Result File Name:script-SERVICIOS_Y_SAP_CUC-VVC.target-CUC_CNT_7210_01.2018-07-16_09-30-38_821.txt.gz
    #Parameters:
    #
    show service service-using | match "Matching"
    Matching Services : 80
    show service sap-using | match "Number"
    Number of SAPs : 80
    show port description | match 10/100/G -> loop
    1/1/4          10/100/Gig Ethernet SFP
    1/1/4          10/100/Gig Ethernet SFP
    1/1/4          10/100/Gig Ethernet SFP
    ...

    #
"""
