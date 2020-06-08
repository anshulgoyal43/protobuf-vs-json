import sys 
import re

if len(sys.argv) != 3:
    print ('Usage:', sys.argv[0] ,'INPUT_FILE','OUTPUT_FILE')
    sys.exit()

name = []
roll = []
cnames = []
cscores = []

with open(sys.argv[1],'r') as ifile:
    line = ifile.readlines()
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

cdata = []

for i in range(0,len(cnames)):
    for j in range(0,len(cnames[i])):
        cdata.append('{'+'"CourseScore"'+':'+cscores[i][j]+','+'"CourseName"'+':'+'"'+cnames[i][j]+'"'+'}')
    record[i] = '{'+'"Name"'+':'+'"'+name[i]+'"'+','+'"CourseMarks"'+':'+'['+",".join(cdata)+']'+','+'"RollNo"'+':'+roll[i]+'}'

with open(sys.argv[2],'w') as ofile:
    ofile.write('['+",".join(record)+']')
