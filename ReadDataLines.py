txtname = 'namedata.txt'


def getnamedata(filename: str):
    openfile = open(txtname, 'r')
    dataresults = openfile.readlines()
    openfile.close()
    return dataresults

print(getnamedata(txtname))
