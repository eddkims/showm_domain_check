import os
import sys
import time
import ctypes
import subprocess
from datetime import datetime

try:
    from scode.util import *
except ImportError:
    subprocess.run(['python', '-m', 'pip', 'install', '--upgrade', 'scode'])
    from scode.util import *

try:
    import whois
except ImportError:
    subprocess.run(['python', '-m', 'pip', 'install', '--upgrade', 'python-whois'])
    import whois


# ===============================================================================
#                            Program infomation
# ===============================================================================

def domain_test():
    print('\n')
    print('list.txt의 도메인을 읽고 등록일을 체크합니다.\n')
    if True :
        domain = "www.naver.com"
        info = whois.whois(domain)
        print(f'info : {info}')
        nowdate = datetime.now()
        startDateTimeStamp = time.mktime(info['updated_date'].timetuple())
        expireDateTimeStamp = time.mktime(info['expiration_date'].timetuple())
        expire_in = info['expiration_date'] - nowdate
        expired_date = str(info['expiration_date']).split(' ')[0]
        print(f'expired_date : {expired_date}')
        #print(f'startDateTimeStamp : {startDateTimeStamp} , expireDateTimeStamp : {expireDateTimeStamp} , leftDays : {expire_in.days}')


def run():
    input_file_path = 'input.txt'
    output1_file_path = 'output1.txt'
    output2_file_path = 'output2.txt'
    output3_file_path = 'output3.txt'
    output4_file_path = 'output4.txt'
    error_file_path = 'error.txt'

    # Inintialize
    open(output1_file_path, 'w').close()
    open(output2_file_path, 'w').close()
    open(output3_file_path, 'w').close()
    open(output4_file_path, 'w').close()

    try:
        input_lst = [x.strip() for x in open(input_file_path).read().splitlines()]
    except UnicodeDecodeError:
        try:
            input_lst = [x.strip() for x in open(input_file_path, encoding='cp949').read().splitlines()]
        except UnicodeDecodeError:
            input_lst = [x.strip() for x in open(input_file_path, encoding='utf-8').read().splitlines()]

    start_time = datetime.now().strftime('%m-%d %H:%M:%S')
    total_count = len(input_lst)
    for idx, domain in enumerate(input_lst, start=1) :
        cur_time = datetime.now().strftime('%m-%d %H:%M:%S')
        if domain == '' :
            print(f'{cur_time}\t{idx}/{total_count}\tline error')
            continue

        domain_info = whois.whois(domain)

        create_date = str(domain_info['creation_date']).split(' ')[0]
        update_date = str(domain_info['updated_date']).split(' ')[0]
        expired_date = str(domain_info['expiration_date']).split(' ')[0]
        registrar = domain_info['registrar']

        print(f'{cur_time}\t{idx}/{total_count}\t{domain}\t등록 {create_date}\t종료 {expired_date}\t등록회사 {registrar}')
        fwrite(output1_file_path, f'{domain}\t{create_date}\t{expired_date}')
        fwrite(output2_file_path, f'{create_date}\t{expired_date}')
        fwrite(output3_file_path, f'{expired_date}')
        fwrite(output4_file_path, f'{domain}\t{registrar}')
        time.sleep(0.1)

    end_time = datetime.now().strftime('%m-%d %H:%M:%S')

    print(f'시작 : {start_time}')
    print(f'종료 : {end_time}')
    print('\n프로그램 종료\n\n')

    '''
    도메인 정보
    info = whois.whois(domain)
    info : {
      "domain_name": "NAVER.COM",
      "registrar": "Gabia, Inc.",
      "whois_server": "whois.gabia.com",
      "referral_url": null,
      "updated_date": "2022-09-20 06:51:25",
      "creation_date": "1997-09-12 04:00:00",
      "expiration_date": "2023-09-11 04:00:00",
      "name_servers": [
        "NS1.NAVER.COM",
        "NS2.NAVER.COM"
      ],
      "status": "clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited",
      "emails": "abuse@gabia.com",
      "dnssec": "unsigned",
      "name": null,
      "org": null,
      "address": null,
      "city": null,
      "state": null,
      "zipcode": null,
      "country": null
    }
    '''


# ===============================================================================
#                            Program infomation
# ===============================================================================

__author__ = '이광헌'
__requester__ = '이광헌'
__registration_date__ = '230112'
__latest_update_date__ = '230112'
__version__ = 'v1.00'
__title__ = '20230112_도메인_등록일_종료일_추출_프로그램'
__desc__ = '20230112_도메인_등록일_종료일_추출_프로그램'
__changeLog__ = {
    'v1.00': ['Initial Release.'],
}
version_lst = list(__changeLog__.keys())

full_version_log = '\n'
short_version_log = '\n'


# ===============================================================================
#                                 Main Code
# ===============================================================================

if __name__ == '__main__':

    ctypes.windll.kernel32.SetConsoleTitleW(f'{__title__} {__version__} ({__latest_update_date__})')

    sys.stdout.write(f'{__title__} {__version__} ({__latest_update_date__})\n')

    sys.stdout.write(f'{short_version_log if short_version_log.strip() else full_version_log}\n')

    run()


