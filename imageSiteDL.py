#! python3
# imageSiteDL.py - Downloads the first 25 images on <site> for the search result

import os
import requests
import sys
import bs4


# Create directory to store image files.
os.makedirs('myImages', exist_ok=True)

# Prompt for selection of websites from list
siteList = [(1, 'Flickr (NOT WORKING)', 'https://www.flickr.com/search/?text='),
            (2, 'Imgur', 'http://imgur.com/search?q='),
            (3, 'pixabay', 'https://pixabay.com/en/photos/?q=')]
for num, site, address in siteList:
    print('{} - {}'.format(num, site))
while True:
    while True:
        try:
            userNum = int(input('\n\nPlease select a number for a site: '))
            break
        except (KeyboardInterrupt, SystemExit):
            raise
        except ValueError:
            print('That was not an integer. Try again.')
    userChoice = [(x, y, z) for x, y, z in siteList if x == userNum]
    if not userChoice:
        print('You didn\'t select a value on the list. Try again.')
    else:
        break

print('You selected {}'.format(userChoice[0][1]))

# Prompt for search term
try:
    userSearch = input('\n\nWhat do you want to search for: ')
except (KeyboardInterrupt, SystemExit):
    raise

# Get web results
res = requests.get(userChoice[0][2] + userSearch)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')

if userNum == 2:
    photoElems = soup.select('.image-list-link img')
elif userNum == 3:
    photoElems = soup.select('img')

# Loop through available photos/images, downloading them, print Done, close file
for item in photoElems[:10]:
    try:
        if userNum == 2:
            imageUrl = 'http:' + item['src']
        elif userNum == 3:
            imageUrl = item['src']
        print('Downloading image {}... '.format(imageUrl), end='')
        res = requests.get(imageUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('myImages', os.path.basename(imageUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        print('Done.')
    except Exception as err:
        print('Something went wrong: {}'.format(err))

# Print finished.
print('Finished.')
