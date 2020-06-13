import os
import sys
import time
import re

line = []

def write(record):
    cdata = []    
    for i in range(1,len(record)-1,2):
        cdata.append(record[i+1]+','+record[i])
    line.append(record[0]+','+record[len(record)-1]+':'+':'.join(cdata))

if len(sys.argv) != 3:
    print ("Usage:",sys.argv[0],"INPUT_FILE","OUTPUT_FILE")
    sys.exit()


with open(sys.argv[1],'r') as data_file:
    
    data = data_file.read()
    start = time.clock()
    ddata = filter(None, re.split('\[|\]|{|"|:|,|}',data))
    record = []
    
    for i in range(0,len(ddata)):
        if ddata[i] == 'Name':
            record.append(ddata[i+1])
        elif ddata[i] == 'CourseScore':
            record.append(ddata[i+1])
        elif ddata[i] == 'CourseName':
            record.append(ddata[i+1])
        elif ddata[i] == 'RollNo':
            record.append(ddata[i+1])
            write(record)
            del record[:]
        
    final = "\n".join(line)
    end = time.clock()
    print "Time taken for conversion :" ,(end - start)*1000 ,"ms"
    print "Rate of Deserialization :" , os.path.getsize(sys.argv[1])/(end-start)*0.001 , "Kbps"

with open(sys.argv[2],"w") as ofile:
    ofile.write(final)
