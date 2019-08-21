## IMPORTS GO HERE

## END OF IMPORTS


#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####

def get_grade (score):                                                #return GPA #PRINT grade
    if score <= 100 and score > 89:
        print ("A+") 
        return 4
    elif score < 90 and score > 85:
        print ("A")
        return 4 
    elif score < 86 and score > 81:
        print ("A-")
        return 3 
    elif score < 82 and score > 77:
        print ("B+")
        return 3 
    elif score < 78 and score > 73:
        print ("B")
        return 3 
    elif score < 74 and score > 69:
        print ("B-")
        return 2 
    elif score < 70 and score > 65:
        print ("C+")
        return 2 
    elif score < 66 and score > 61:
        print ("C")
        return 2 
    elif score < 62 and score > 57:
        print ("C-")
        return 1 
    elif score < 58 and score > 53:
        print ("D+")
        return 1 
    elif score < 54 and score > 49:
        print ("D")
        return 1
    elif score < 50 and score > -1:
        print ("F")
        return 0
    else:
        return None


#### End OF MARKER




if __name__ == '__main__':
    print (get_grade(50))
    print(calculate_sgpa('A', 'B', 'nothing'))
