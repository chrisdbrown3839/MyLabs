#https://www.youtube.com/watch?v=CqvZ3vGoGs0

#import basic_module
#import basic_module as bm
from basic_module import find_index

import net_module

def main():
    test = "nnn"
    networks = ['CWAN', 'ACI', 'SNE05', 'SNE06']
    # Local function
    #(result, index) = find_index(networks, test)

    # using import
    #(result, index) = basic_module.find_index(networks, test)

    # using import as bm
    #(result, index) = bm.find_index(networks, test)

    # using from import
    (pos, value) = find_index(networks, test)

    print(f'{pos}: {value}')

    #net_module.list_hosts('172.31.168.192/27')
    subnet = net_module.list_hosts('172.31.168.192/27')
    print(subnet)



# def find_index(to_search, target):
#     #Find the index of a value in a sequence
#
#     for index, value in enumerate(to_search):
#         if value == target:
#             return index, target
#
#     return -1,'na'

main()