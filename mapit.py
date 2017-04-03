#! python3
# mapIt.py - Launches a map in the browswer using an address from the command line
# or clipboard.


import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # get address from command line
    # sys.argv is a list of strings
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

# replaced maps/place with maps/search so you can ask for directions
webbrowser.open('https://www.google.com/maps/search/' + address)
