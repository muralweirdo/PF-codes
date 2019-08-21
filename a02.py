## IMPORTS GO HERE
  
from scipy.constants import c

## END OF IMPORTS 


#### YOUR CODE FOR calculate_force GOES HERE ###

def calculate_force (mass,acceleration):
    if type(mass)==float and type(acceleration)==float:
        force = mass * acceleration
        return force
    else:
        return None

#### End OF MARKER


#### YOUR CODE FOR find_and_print_energy GOES HERE ###

def find_and_print_energy (mass):
    if type(mass)==float:
        energy = mass *pow(c,2)
        print ("The energy equivalent of mass" ,mass,"is:",energy)
        return energy
    else:
        return None

#### End OF MARKER  




if __name__ == '__main__': 
    print(calculate_force(1.0, 0.2))
    print(find_and_print_energy(0.0009))  

