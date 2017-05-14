import time
import os
import sys

mydict = {'Jack': [15, 'brown'], 'Jill': [10, 'black'],'Jeff': [9, 'blonde']}

print(mydict['Jack'])

mydict['Cara'] = [24, 'blonde']
print(mydict)

del mydict['Jill']
print(mydict)

print(abs(-5))

time.sleep(1)

print('Done!')

print(int(55.0))
print(type(33))

curDir = os.getcwd()
print(curDir)

os.mkdir('ExampleCodeSnippets')

os.listdir(curDir)
