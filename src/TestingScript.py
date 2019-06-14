import random
import os
import string

def lol():
    newMAC = "";


    smallletters = string.ascii_lowercase
    bigletters = string.ascii_uppercase

    for x in range(6):
        newMAC = newMAC + ":";
        for y in range(2):
            newMAC = newMAC + str(random.randint(1,9));

    newMAC = newMAC[1:];
    print(newMAC);

lol();