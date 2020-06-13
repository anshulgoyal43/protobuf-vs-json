import sys
import re
import time
import os

if len(sys.argv) != 3:
    print ('Usage:', sys.argv[0] ,'INPUT_FILE','OUTPUT_FILE')
    sys.exit()

name = []
roll = []
cnames = []
cscores = []
records = []

with open(sys.argv[1],'r') as ifile:
    line = ifile.readlines()
    start = time.clock()
    for i in range(0,len(line)):
        record = re.split(':|,|\n',line[i])
        name.append(record[0])
        roll.append(record[1])
        cname = []
        cscore = []
        for j in range(2,len(record)-1,2):
            cname.append(record[j])
            cscore.append(record[j+1])
        cnames.append(cname)
        cscores.append(cscore)


for i in range(0,len(cnames)):
    cdata = []
    for j in range(0,len(cnames[i])):
        cdata.append('{'+'"CourseScore"'+':'+cscores[i][j]+','+'"CourseName"'+':'+'"'+cnames[i][j]+'"'+'}')
    records.append('{'+'"Name"'+':'+'"'+name[i]+'"'+','+'"CourseMarks"'+':'+'['+",".join(cdata)+']'+','+'"RollNo"'+':'+roll[i]+'}')

final = '['+",".join(records)+']'


end = time.clock()

print "Time taken for conversion :",(end - start)*1000 ,"ms"
print "Rate of Serialization :", os.path.getsize(sys.argv[1])/(end-start)*0.001 , "Kbps"

with open(sys.argv[2],'w') as ofile:
    ofile.write(final)

