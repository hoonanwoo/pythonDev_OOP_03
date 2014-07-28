#!/usr/bin/python env
""" getError.py
This program will parse an xml file for the 'Error' element and return
the associated string
"""

from xml.etree.ElementTree import parse
from time import asctime

timeStampFileWrite = asctime()

dParse = parse('C:\Users\Public\pythonCode\errorXML.xml')
fileStore = 'fileParseAstraLog_errors.txt'


def parseXML():
   
    try:
        fileOpen = open(fileStore,'a')
    except IOError:
        print "[Errno 22] invalid mode"
   
    fileOpen.writelines(timeStampFileWrite + '\n\n')

    for xmlTag in dParse.findall('Log'):
        stringMessage = xmlTag.findtext('Message')       
        stringCategory = xmlTag.findtext('Category')
        stringSource = xmlTag.findtext('Source')

        if stringCategory == 'ViewInstructions':    
            fileOpen.writelines(stringMessage)
            fileOpen.writelines(stringSource)
            
   
if __name__ == '__main__':
    parseXML()
