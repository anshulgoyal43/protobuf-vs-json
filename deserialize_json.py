import json
import sys
import time
import re

def write(record):
    line = []
    cdata = []    
    for i in range(1,len(record)-1,2):
        cdata.append(record[i+1]+','+record[i])
    line.append(record[0]+','+record[len(record)-1]+':'+':'.join(cdata)+'\n')
    ofile.write(line[0])
   # print line[0]
        

if len(sys.argv) != 3:
    print ("Usage:",sys.argv[0],"INPUT_FILE","OUTPUT_FILE")
    sys.exit()


with open(sys.argv[1],'r') as data_file:
    
    data = data_file.read()
    ddata = filter(None, re.split('\[|\]|{|"|:|,|}',data))
    record = []
    ofile = open(sys.argv[2],"w")
    
    for i in range(0,len(ddata)):
        if ddata[i] == 'Name':
            record.append(ddata[i+1])
        elif ddata[i] == 'CourseScore':
            record.append(ddata[i+1])
        elif ddata[i] == 'CourseName':
            record.append(ddata[i+1])
        elif ddata[i] == 'RollNo':
            record.append(ddata[i+1])
#            print record
            write(record)
            del record[:]

