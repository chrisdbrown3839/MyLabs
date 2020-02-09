import ipaddress

def list_hosts(subnet):
    rangelist =[]
    '''Show IP hosts in a subnet'''
    net4 = ipaddress.ip_network(subnet)
    for x in net4.hosts():
        print(x)
        x = str(x)

        rangelist.append(x)
    return rangelist