import sys
import re

if len(sys.argv) != 3:
    print ('Usage:', sys.argv[0] ,'INPUT_FILE','OUTPUT_FILE')
    sys.exit()

name = []
roll = []
tname = []
tscore = []

with open(sys.argv[1],'r') as ifile:
    line = ifile.readlines()
    for i in range(0,len(line)):
        record = re.split(':|,|\n',line[i])
        name.append(record[0])
        roll.append(record[1])
        cnames = []
        cscores = []
        for j in range(2,len(record)-1,2):
            cnames.append(record[j])
            cscores.append(record[j+1])
        tname.append(cnames)
        tscore.append(cscores)

cdata = []

for i in range(0,len(tname)):
    for j in range(0,len(tname[i])):
        cdata.append('{'+'"CourseScore"'+':'+tscore[i][j]+','+'"CourseName"'+':'+'"'+tname[i][j]+'"'+'}')
    record[i] = '{'+'"Name"'+':'+'"'+name[i]+'"'+','+'"CourseMarks"'+':'+'['+",".join(cdata)+']'+','+'"RollNo"'+':'+roll[i]+'}'

with open(sys.argv[2],'w') as ofile:
    ofile.write('[')
    ofile.write(",".join(record))
    ofile.write(']')
