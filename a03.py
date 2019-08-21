## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR good_enough() FUNCTION GOES HERE ####

def good_enough (n,g):
    if abs(g*g-n) < 0.1:
        return True
    else:
        return False

#### End OF MARKER


#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####

def sqrt (n,g=0):
    count=1
    if good_enough(n,g):
        return (g)
    else:
        g = improve_guess(n,g)
        count=count+1
        a =  sqrt(n,g)
        print("Took: ",count," steps")
        return a

#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####

def improve_guess (n,g):
    if g==0:
        g=g+0.1
        g = g-( ((g*g)-n)/(2*g) )
        return g
    else:
        g = g-( ((g*g)-n)/(2*g) )
        return g

#### End OF MARKER




if __name__ == '__main__':
    print(sqrt(36))
