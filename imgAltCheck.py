#! /usr/bin/env python3

# imgAltCheck - Read HTML file to verify that all img tags have a
#     corresponding alt tag.
# USAGE: Currently under development.
# VERSION: 03/16/2017

import os
import sys
import urllib
import urllib.request


response = urllib.request.urlretrieve('https://gitlab.com/lotspaih',
                                      'imgalt.html')

with open('imgalt.html', 'r') as HTMLfile:
    try:
        HTMLlines = HTMLfile.readlines()
    except:
        print('Is this a link to an HTML file?')
        sys.exit(1)

lineNumber = 0
for line in HTMLlines:
    lineNumber += 1
    if 'img src=' not in line:
        continue
    elif 'alt=' not in line:
        print('Line number: {} contains an image source tag without a '
              'coressponding alternative text tag!'.format(lineNumber))

if os.name == 'nt':
    print('')
    os.system('pause')
else:
    print('')
    input('Press Return/Enter to continue...')
sys.exit(0)
