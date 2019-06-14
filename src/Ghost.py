import random
import os
import string
import subprocess
import socket
import multiprocessing


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

    os.system("chmod 777 /etc/hostname")

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
    os.system("sudo apt-get install macchanger")
    os.system("sudo ifconfig wlp1s0 down")
    os.system("sudo macchanger -m "+ GenerateNewRandomMAC() +" wlp1s0")
    os.system("sudo ifconfig wlp1s0 up")

    print("MAC address changed")

def GenerateNewRandomMAC():
    print("Generating random MAC address")

    newMAC = "";


    smallletters = string.ascii_lowercase
    bigletters = string.ascii_uppercase

    for x in range(6):
        newMAC = newMAC + ":";
        for y in range(2):
            newMAC = newMAC + str(random.randint(1,9));

    newMAC = newMAC[1:];
    return newMAC;


############################################
# The Ip segemnt of the script just for gathering the ip-s;
def pinger(job_q, results_q):
    """
    Do Ping
    :param job_q:
    :param results_q:
    :return:
    """
    DEVNULL = open(os.devnull, 'w')
    while True:

        ip = job_q.get()

        if ip is None:
            break

        try:
            subprocess.check_call(['ping', '-c1', ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass


def get_my_ip():
    """
    Find my IP address
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def map_network(pool_size=255):
    """
    Maps the network
    :param pool_size: amount of parallel ping processes
    :return: list of valid ip addresses
    """

    ip_list = list()

    # get my IP and compose a base like 192.168.1.xxx
    ip_parts = get_my_ip().split('.')
    base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'

    # prepare the jobs queue
    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [multiprocessing.Process(target=pinger, args=(jobs, results)) for i in range(pool_size)]

    for p in pool:
        p.start()

    # cue hte ping processes
    for i in range(1, 255):
        jobs.put(base_ip + '{0}'.format(i))

    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()

    # collect he results
    while not results.empty():
        ip = results.get()
        ip_list.append(ip)

    return ip_list

############################################################



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

#TODO: Generate a random IP form the list below
#TODO: Assing the ip

if __name__ == '__main__':

    print('Mapping...')
    lst = map_network()
    print(lst)





