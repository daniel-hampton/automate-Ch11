#! python3
# weather.py - Launches the weather forecast in the browswer using an address from the command line
# or clipboard.


import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # get address from command line
    # sys.argv is a list of strings
    zipcode = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    zipcode = pyperclip.paste()

webbrowser.open('https://www.wunderground.com/cgi-bin/findweather/getForecast?query='
                + zipcode)
