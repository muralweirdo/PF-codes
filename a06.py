
### Code for get_grades starts here 

grades={'A': 80, 'B': 70, 'C': 60, 'D': 50}

def get_grade(score, grades):
    for i in grades:
        if score >= grades['A']:
            return ("A")
        if score >= grades['B']:
            return ("B")
        if score >= grades['C']:
            return ("C")
        if score >= grades['D']:
            return ("D")
        if score >= 0:
            return ("F")

### END MARKER 



### Code for get_student_marks starts here 

def get_student_marks (a):
    
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    sum6=0
    
    for i in a[0]['marks']['english']:
        if i == None:
            i=0
        sum1=sum1+i
    for j in a[0]['marks']['calculus']:
        if j == None:
            j=0
        sum2=sum2+j
    for k in a[1]['marks']['english']:
        if k == None:
            k=0
        sum3=sum3+k
    for l in a[1]['marks']['programming fundaments']:
        if l == None:
            l=0
        sum4=sum4+l
    for m in a[2]['marks']['calculus']:
        if m == None:
            m=0
        sum5=sum5+m
    for n in a[2]['marks']['programming fundamentals']:
        if n == None:
            n=0
        sum6=sum6+n
            
    
    print({
        'p18-1001': {'english': sum1,
                     'calculus': sum2
                    },
        'p18-1002': {'english': sum3,
                     'programming fundaments': sum4
                    },
        'p18-1003': {'calculus': sum5,
                     'programming fundamentals': sum6
                    }
    })

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








 