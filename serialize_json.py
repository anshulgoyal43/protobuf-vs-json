import sys
import json
import time
import os
from collections import OrderedDict

if len(sys.argv) != 3:
    print "Usage:", sys.argv[0], "INPUT_FILE" , "OUTPUT_FILE"
    sys.exit(1)

with open(sys.argv[1]) as data_file:
    data = data_file.readlines()

final_list = []
for record in data:
  list_record = record.split(":")
  dict_record = OrderedDict()
  dict_record["Name"] = list_record[0].split(",")[0]
  list_marks = []
  for i in range(1,len(list_record)):
    dict_marks = OrderedDict()
    course_name = list_record[i].split(",")[0]
    course_marks = int(list_record[i].split(",")[1])
    dict_marks["CourseScore"] = course_marks
    dict_marks["CourseName"] = course_name
    list_marks.append(dict_marks)
  dict_record["CourseMarks"] = list_marks
  dict_record["RollNo"] = int(list_record[0].split(",")[1])
  final_list.append(dict_record)

with open(sys.argv[2], 'w') as outfile:
    start = time.clock()
    json.dump(final_list, outfile, separators=(',', ':'),ensure_ascii=False)
    end = time.clock()

print "Serialization time", end - start
