
### Code for get_grades starts here 
def get_grade(m,d):
    m = float(m)
    d= {'A': 80, 'B': 70, 'C': 60, 'D': 50}
    if  m >= 80: return "A"
    if  80 > m >= 70: return "B"
    if  70 > m >= 60: return "C"
    if  60 > m >= 50: return "D"
    if  50 > m: return "F"
### END MARKER 

### Code for get_student_marks starts here 
d =[
{'roll_no': 'p18-1001', 'marks': {
'english': (1.4, 2.5, 15, 9.6, 33),
'calculus': (2.4, 1.5, 12, 1.6, 21),
}, 'attendance': 88.4
},
{'roll_no': 'p18-1002', 'marks': {
'english': (2.4, 1.5, 12, 1.6, 21),
'programming fundaments': (2.4, 1.5, 12, 1.6, 21),
}, 'attendance': 79.4
},
{'roll_no': 'p18-1003', 'marks': {
'calculus': (2.4, 1.5, 12, None, 21),
'programming fundamentals': (2.4, 1.5, 12, 1.6, 21),
}, 'attendance': 79.4
},
]
def get_student_marks(d):
    R={}
    for i in d:
        a=d[0]['marks']['english']
        b=d[0]['marks']['calculus']
        c=sum(a,b)
        print (c)
### END MARKER 

if __name__ == '__main__': 
    grade_boundaries = {'A': 80, 'B': 70, 'C': 60, 'D': 50}
    
    student_data = [ 
        {'roll_no': 'p18-1001', 'marks': {
                'english': (1.4, 2.5, 15, 9.6, 33), 
                'calculus': (2.4, 1.5, 12, 1.6, 21),
            }, 'attendance': 88.4
        }, 
        {'roll_no': 'p18-1002', 'marks': {
                'english': (2.4, 1.5, 12, 1.6, 21),
                'programming fundaments': (2.4, 1.5, 12, 1.6, 21),
            }, 'attendance': 79.4
        }, 
        {'roll_no': 'p18-1003', 'marks': {
                'calculus': (2.4, 1.5, 12, None, 21), 
                'programming fundamentals': (2.4, 1.5, 12, 1.6, 21), 
            }, 'attendance': 79.4
        }, 
    ]


    # print(student_data)
    student_marks = get_student_marks(student_data)
    print(student_marks)

    print(get_grade(80, grade_boundaries))








 