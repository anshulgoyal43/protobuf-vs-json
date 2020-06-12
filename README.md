Programs to perform comparison with respect to time and rates of serialization/deserialization between Json and Google Protobuf (samples attached).  

Input Record Format:```<Name>,<RollNo>:<Course1>,<Marks1>:<Course2>,<Marks2>:...:<CourseN>,<MarksN>```

**Example**:  
Bhavesh,201301116:cs210,85:cs155,94  
Dhruva, 201301151:cs210,20:cs155,47 

Json format:
[{\
"Name": "Bhavesh", "CourseMarks": [{\
"CourseScore": 85, "CourseName": "cs125"\
}, {\
"CourseScore": 94, "CourseName": "cs210"\
}],\
"RollNo": 165\
}, {\
"Name": "Dhruva", "CourseMarks": [{\
"CourseScore": 20, "CourseName": "cs125"\
}, {"CourseScore": 37, "CourseName": "cs210"\
}],\
"RollNo": 169\
} ]\
