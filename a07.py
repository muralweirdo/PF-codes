## IMPORTS GO HERE
import os
## END OF IMPORTS


### YOUR CODE FOR split_safe() FUNCTION GOES HERE ###

def split_safe (my_string):
    count = 0
    final_list = []
    imp_word = ""
    
    for i in my_string:
        if i != ",":
            imp_word += i
            count += 1
            
        elif i == "," or i == my_string[-1]:
            imp_word = imp_word.strip()
            
            if imp_word[0] == "'":
                if imp_word[-1] != "'":
                    imp_word += ","
                    
                elif imp_word[-1] == "'":
                    imp_word = imp_word[1:-1]
                    final_list.append(imp_word)
                    imp_word = ""   
            else:
                final_list.append(imp_word)
                imp_word = " "
                count += 1
    
    if count == 0:
        return (final_list)
    elif imp_word[0] and imp_word[-1] is "'":
        imp_word = imp_word[1:-1]
        
    imp_word = imp_word.strip()
    final_list.append(imp_word)
    return (final_list)


#### End OF MARKER



### YOUR CODE FOR read_data() FUNCTION GOES HERE ###

dir_name="mine"
file_name="file.csv"
def read_data(dir_name,file_name):
    new_path=os.path.join(dir_name,file_name)
    final=[]
    f=open(new_path,"r")
    for line in f:
        old_split=split_safe(line)
        final.append(old_split)
    return (final)
    f.close()

#### End OF MARKER

if __name__ == '__main__':
    print(split_safe("Name,'Father Name',Address,Age"))
    print(split_safe("Ali,Tariq,'House 10, Street 20',30"))

    print(read_data('', 'file.csv'))
    pass
