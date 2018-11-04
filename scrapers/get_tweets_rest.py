#! usr/bin/env python
# *-- coding: utf-8 --*


import requests


def main():
    url = 'https://twitter.com/anyuser/status/'
    r = requests.get(url + '/591902701967007744')
    if r.status_code == 200:
        print(r.text)


if __name__ == '__main__':
    main()


