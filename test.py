import os
import sys
import re
import time
import ctypes
import subprocess
import socket
try:
    from ipwhois import IPWhois
except ImportError:
    subprocess.run(['python', '-m', 'pip', 'install', '--upgrade', 'ipwhois'])
    from ipwhois import IPWhois

try:
    from cymruwhois import Client
except ImportError:
    subprocess.run(['python', '-m', 'pip', 'install', '--upgrade', 'cymruwhois'])
    from cymruwhois import Client

from scode.selenium import *


# ===============================================================================
#                               Definitions
# ===============================================================================

def run():
    
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'
    error_file_path = 'error.txt'
    
    # Inintialize
    open(output_file_path, 'w').close()
    open(error_file_path, 'w').close()

    ips = ['windowmmoniter.shop']
    for ip in ips:
        try :
            addy = "".join(ip)
            obj = IPWhois(addy)
            results = obj.lookup(get_referral=True)
            
            query = results['query']
            nets = None
            if results['nir'] == None : 
                nets = results['nets'][0]
            else : 
                nets = results['nir']['nets'][0]
            
            name =  nets['name'].replace('\n','').replace(",","")
            country = nets['country'].replace('\n','').replace(",","")
            address = nets['address'].replace('\n','').replace(",","")
            #ip2 = results['query'] + "," + results['nets'][0]['name'] + "," + results['nets'][0]['country'].rstrip('\n') + "," + results['asn']
            result =  query + ',' + name+  ',' + country + ',' + address
            print (result) 

        except :
            pass


    # TODO: 기능구현

# ===============================================================================
#                            Program infomation
# ===============================================================================

__author__ = '김홍연'
__requester__ = '요청자'
__registration_date__ = '230116'
__latest_update_date__ = '230116'
__version__ = 'v1.00'
__title__ = '230112 도메인 등록일 종료일 확인 프로그램 (2)'
__desc__ = '230112 도메인 등록일 종료일 확인 프로그램 (2)'
__changeLog__ = {
    'v1.00': ['Initial Release.'],
}
version_lst = list(__changeLog__.keys())

full_version_log = '\n'
short_version_log = '\n'

for ver in __changeLog__:
    full_version_log += f'{ver}\n' + '\n'.join(['    - ' + x for x in __changeLog__[ver]]) + '\n'

if len(version_lst) > 5:
    short_version_log += '.\n.\n.\n'
    short_version_log += f'{version_lst[-2]}\n' + '\n'.join(['    - ' + x for x in __changeLog__[version_lst[-2]]]) + '\n'
    short_version_log += f'{version_lst[-1]}\n' + '\n'.join(['    - ' + x for x in __changeLog__[version_lst[-1]]]) + '\n'

# ===============================================================================
#                                 Main Code
# ===============================================================================

if __name__ == '__main__':

    ctypes.windll.kernel32.SetConsoleTitleW(f'{__title__} {__version__} ({__latest_update_date__})')

    sys.stdout.write(f'{__title__} {__version__} ({__latest_update_date__})\n')

    sys.stdout.write(f'{short_version_log if short_version_log.strip() else full_version_log}\n')

    run()