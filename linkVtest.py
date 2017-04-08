#! python3
# linkVtest.py - copied code from linVerification.py with slight adjustments to test a local html file
# for broken links.

import requests
import bs4
import sys
from urllib.parse import urljoin

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

file = open('example.html')
soup = bs4.BeautifulSoup(file, 'lxml')  # create BeautifulSoup object
file.close()

linkElem = soup.select('a[href]')  # find all links on page

brokenLinks = []  # prep empty list for later

# Loop through all found links checking for exceptions. 404 exceptions are placed in brokenLinks list.
for tag in linkElem:
    try:
        link = tag.get('href')
        # if not link.startswith('http'):  # creates absolute url from relative urls.
        #     link = urljoin(url, link)
        print('Checking: {} ... '.format(link), end='')
        res = requests.get(link, headers=headers)
        if res.status_code == 200:
            print('OK')
        elif res.status_code == 404:
            brokenLinks.append(link)
            print('NOT FOUND... ', end='')
        res.raise_for_status()
    except requests.RequestException as err:
        print('Something went wrong:  {}'.format(err))
        print(str(res.status_code))

# Prints out list of broken links.
print('\nThe following links were broken:\n')
for x in brokenLinks:
    print(x)

print('\n' + headers['User-Agent'])
