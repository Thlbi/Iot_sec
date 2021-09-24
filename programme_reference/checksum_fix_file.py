# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 18:14:38 2021

@author: thiba
"""


# import os

# Get the current working directory
# cwd = os.getcwd()

# Print the current working directory
# print("Current working directory: {0}".format(cwd))

# data=':10455000068183207F0FE07FC0210501301C40369B'

def sum_words(data):
    return sum(int(x, 16) for x in data)


def checksum(data):
    data2 = [data[i:i + 2] for i in
             range(1, len(data) - 4, 2)]  # on enlève les : + l'indicateur de fin de ligne + le checksum actuel
    print(data2)
    sum = sum_words(data2)
    sum = (sum & 0x00FF)
    sum2 = (sum ^ 0x00FF)
    CC = hex(sum2 + 1)
    print(CC)
    return CC[2:]


def checksumFile(filename):
    filin = open(filename, 'r')
    lignes = filin.readlines()
    i_ligne = 0

    for ligne in lignes:
        CC = checksum(ligne)
        lignes[i_ligne] = ligne[:-3] + CC.upper() + '\n'

        i_ligne += 1

    print(lignes)

    filout = open(filename, 'w')
    filout.writelines(lignes)
    filin.close()
    filout.close()


checksumFile('file.txt')
