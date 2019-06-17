import os
import socket
import multiprocessing
import subprocess
import os
import random;


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

def GhatherIPData():
    ip0 = lst[0];
    ip1 = lst[1];

    ipA0 = ip0.split(".");
    ipA1 = ip1.split(".");

    print(ipA0);
    print(ipA1);

    mask_number = 0;

    if(ipA1[0] == ipA0[0]):
        mask_number += 8;
        print(ipA1[0])
        print("Network mask = 8 bit")

    if(ipA1[1] == ipA0[1]):
        mask_number += 8;
        print(ipA1[1])
        print("Network mask = 16 bit")

    if(ipA1[2] == ipA0[2]):
        mask_number += 8;
        print(ipA1[2])
        print("Network mask = 24 bit")

    if(ipA1[3] == ipA0[3]):
        mask_number += 8;
        print(ipA1[3])
        print("Network mask = 32 bit")


    print("Final network mask is: " + str(mask_number) + " Bit");

def MakeTakenIpsList( listOfIps):
    takenNummbers = [];

    for Ips in listOfIps:
        currentIp = Ips.split(".");
        takenNummbers.append(currentIp[3]);

    print("IPs taken: " + str(takenNummbers));
    return takenNummbers;

def GenerateNewIp():
    takenIPs = MakeTakenIpsList(lst);

    newIP = GetNewIp();

    for x in takenIPs:
        if(newIP == x):
            newIP = GetNewIp();
        else:
            listIP = lst[0].split(".")
            del listIP[-1]
            listIP.append(newIP);
            break;

    IP = str(listIP[0]) + "." + str(listIP[1]) + "." + str(listIP[2]) + "." + str(listIP[3])
    return IP;


def GetNewIp():
    newIP = random.randint(3, 240);
    return newIP;

if __name__ == '__main__':

    print('Mapping...')
    lst = map_network()
    print(lst)
    GhatherIPData();
    print(GenerateNewIp());


