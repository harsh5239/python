import csv

fields=['student_name' ,' marks' , 'age' , 'contact' , 'study_hours']
rows=[['harsh','99','88','869646','2'],
     ['harsha','44','21','233333','4'],
       ['harshitac','48','21','213333','6'],
       ['harshita','86','21','23112','3'],
     ]
filename='stu1.csv'
f=open('stu1.csv','w')
writer=csv.writer(f)
writer.writerow(fields)
writer.writerows(rows)

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('stu1.csv')
name=df['student_name']
marks=df['marks']
age=df['age']
mob=df['contact']
hrs=df['study_hours']
plt.pie(marks,labels=name,autopct=%1.1f%%)
plt.pie(age,labels=name,autopct=%1.1f%%)
plt.pie(hrs,labels=name,autopct=%1.1f%%)
