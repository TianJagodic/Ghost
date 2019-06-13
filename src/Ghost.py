import random
import os
import sys


HostnamePath = "/etc/hostname";

def ReWriteHostname():
    w=open(HostnamePath, "w")
    if w.mode == "w":
        w.write(str(random.random()));
        print("Hostname rewriten succsesfuly")



def FindHostname():
    f = open(HostnamePath, "r")
    if f.mode == 'r':
        contents = f.read()
        if contents != "":
            print("Hostname File Found...")
            print("Rewriting the Hostname file...")
            ReWriteHostname();


print("Start up...")
FindHostname()
