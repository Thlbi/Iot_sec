# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 18:14:38 2021

@author: thiba
"""
import os

# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))

data=':10240400736F636F6765746563682F534543524503'

def sum_words(data):
    return sum(int(x, 16) for x in data)


def checksum(data):
    data2=[data[i:i+2] for i in range(1, len(data)-4, 2)] # on enlève les : + l'indicateur de fin de ligne + le checksum actuel
    print(data2)
    sum=sum_words(data2)
    sum=(sum & 0x00FF)
    sum2=(sum ^ 0x00FF)
    CC= hex(sum2+1)
    print(CC)
    return CC[2:]

def checksumFile(filename):
    filin = open(filename,'r')
    lignes = filin.readlines()
    i_ligne = 0
    donnees=[]
    for ligne in lignes :
        if ligne[8]=="0":
            donnees.append(ligne[9:-3])
        i_ligne += 1
    print(donnees)
    filin.close()
    n=5

    tab=[]


    for i in range(len(donnees)):
        nbcarac=0
        data=donnees[i]
        chaine = ""
        for j in range(0,len(data),2):
            val=data[j:j+2]
            val2=int(val,16)
            c=chr(val2)
            if (c.isprintable()):
                nbcarac+=1
            chaine+=c
        if (nbcarac>5):
            print(chaine)
        nbcarac=0
            #c.isprintable()
#on prend en compte les caractères affichables (de 20 à 7D

checksumFile('firmware_tp3_v2.33.hex')

#checksum(data)
