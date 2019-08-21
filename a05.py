## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####

def is_prime(num):
    factors = 0
    if num > 1:
        for i in range(2 , round(num) ):
            if(round(num) % i == 0):
                factors = factors + 1 
        if(factors <= 0):
            return True
        else:
            return False

#### End OF MARKER

#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####

def output_factors(numb):
    for i in range(1, numb + 1):
        if numb % i == 0:
            print (i)

#### End OF MARKER

#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####

def get_largest_prime(number):
    if number < 2:
        return None
    else:
        for i in range(1,round(number)+1):
            if is_prime(i):
                ha = i
        return(ha)

#### End OF MARKER



if __name__ == '__main__':
    print(is_prime(499))  # should return True

    print(get_largest_prime(10))  # should return 7
    # print get_largest_prime(100000)  # bonus, try with 100k

    output_factors(10)  # should output -- 1 2 5 10 -- one on each line
