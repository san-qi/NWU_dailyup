from aes_crypt import MyAes
from bs4 import BeautifulSoup
from json import load
from random import randint
from time import sleep, ctime
import os
import re
import requests
import sys

__DEBUG = False     # or 'True'


def report(name, passwd, report_data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/80.0.3987.149 Safari/537.36'
    }
    s = requests.Session()
    s.cookies.set('org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE', 'zh_CN')
    s.headers = headers
    index_url = 'https://app.nwu.edu.cn/ncov/wap/open-report/save'
    index_page = s.get(index_url)
    data = {'username': name,
            'password': passwd,
            }
    soup = BeautifulSoup(index_page.text, 'html.parser')
    for tag in soup.select('#casLoginForm > input[type=hidden]'):
        data[tag['name']] = tag['value']
    result = re.search(r'var pwdDefaultEncryptSalt = "(\S*)"', index_page.text)
    key = result.group(1)
    aes = MyAes(key)
    data['password'] = aes.encrypt(data['password'])
    login_url = 'http://authserver.nwu.edu.cn' + soup.select_one('#casLoginForm')['action']
    s.post(login_url, data=data)
    headers['X-Requested-With'] = 'XMLHttpRequest'
    if not __DEBUG:
        sleep(4)
    r = s.post('https://app.nwu.edu.cn/ncov/wap/open-report/save', headers=headers, data=report_data)
    print('\t', r.text)
    s.close()

def solve(json_data):
    for (key, value) in json_data['user'].items():
        if key:
            print(key, "start:")
            if not __DEBUG:
                sleep(randint(17, 39))
            report(key, value, json_data['msg'])


if __name__ == '__main__':
    work_dir = sys.argv[1]
    os.chdir(work_dir)
    with open('data.json') as file:
        json_data = load(file)
    solve(json_data)
    print(ctime(), 'reported', '\n'*2)
