import random
import os
import subprocess

HostnamePath = "/etc/hostname";

def ReWriteHostname():
    #Write a random float to the host name file
    w=open(HostnamePath, "w")
    if w.mode == "w":
        newName = str(random.random());
        newName = newName[1:];
        newName = newName[1:];
        w.write(str(newName));
        print("Hostname rewriten succsesfuly")



def FindHostname():
    #Try to find the hostname file NOTE: it does not have a type like .txt
    f = open(HostnamePath, "r")
    if f.mode == 'r':
        contents = f.read()
        if contents != "":
            print("Hostname File Found...")
            print("Rewriting the Hostname file...")
            ReWriteHostname();


def WriteNewMACaddress():
    print("Starting with the MAC address...")
    os.system("ifconfig eth0 down")
    os.system("ifconfig eth0 hw ether 00:80:48:BA:d1:30")
    os.system("ifconfig eth0 up")
    os.system("ifconfig eth0 |grep HWaddr")

    print("MAC address changed")



##########################
#We Start here and go down.
##########################
print("Start up...")
print("Getting root privilages...")


#Get user root id
euid = os.geteuid()
if euid != 0:
    print("Error with root...Exiting")
    exit();


FindHostname();
WriteNewMACaddress();
