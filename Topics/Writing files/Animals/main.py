# read animals.txt
# Reading files module, section "readlines()".  
Literally copy the code without the comments.  
    
# and write animals_new.txt
animals_new.txt = open('animals_new.txt', 'w', encoding='utf-8')
# Writing files module, section "Writing multiple lines".  Copy lines 3 through 9.  

str.rstrip('\n') + ' '
animals.txt.close()
animals_new.txt.close()

#Now you will have to think about about how to integrate the two sections of code.  
    1) For example, should you be printing the "print(file.readlines())" line in step 2 or storing it so you can use it step 3?
    2) The file name in step 3 need to be change to the new file name
for el in animal:
    lst_animal.append(el.rstrip())
