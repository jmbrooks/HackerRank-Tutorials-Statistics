# Reads file, if empty, adds lines to it. If only has beginning lines, appends, if has all, reads all as correct

txtfilename = 'exampleFile.txt'


def readtext(filename: str) -> str:
    print(filename)

    openfile = open(filename, 'r')
    filetext = openfile.read()

    openfile.close()
    return filetext


def writetext(filename: str) -> object:
    print('Writing correct text to file...')

    filetext = 'Here is the proper text!'
    openappfile = open(filename, 'w')
    openappfile.write(filetext)

    print('Done.')
    openappfile.close()
    return openappfile

if readtext(txtfilename) is None:
    print('Text was not there.')
elif readtext(txtfilename) == '':
    print(readtext(txtfilename))
    writetext(txtfilename)
    print(readtext(txtfilename))
else:
    print('Correct Text!')
