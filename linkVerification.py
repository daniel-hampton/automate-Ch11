#! python3
# linkVerification.py - takes a user supplied url and checks all links on page for 404 "Not Found" errors
# and prints them out as broken links

import requests
import bs4
import sys
from urllib.parse import urljoin

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

while True:  # Gets user URL from keyboard. Allows exit and handles exceptions.
    try:
        url = input('\n\nPlease enter the url to check for broken links (Exit to leave): \n')
        if url.lower() == 'exit':
            print('\n\nExiting program...')
            sys.exit(99)
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        break
    except Exception as err:
        print('An error has occurred with the URL:  {}'.format(err))

soup = bs4.BeautifulSoup(res.text, 'lxml')  # create BeautifulSoup object

linkElem = soup.select('a[href]')  # find all links on page

brokenLinks = []  # prep empty list for later

# Loop through all found links checking for exceptions. 404 exceptions are placed in brokenLinks list.
for tag in linkElem:
    try:
        link = tag.get('href')
        if not link.startswith('http'):  # creates absolute url from relative urls.
            link = urljoin(url, link)
        print('Checking: {} ... '.format(link), end='')
        res = requests.get(link, headers=headers)
        if res.status_code == 200:
            print('OK')
        if res.status_code == 404:
            brokenLinks.append(link)
            print('NOT FOUND... ', end='')
        res.raise_for_status()
    except requests.RequestException as err:
        print('Something went wrong:  {}'.format(err))

# Prints out list of broken links.
print('\nThe following links were broken:\n')
for x in brokenLinks:
    print(x)
