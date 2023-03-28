#### Random Password Generator in Python ###
### PROGRAM MADE BY HEMENDRA NAIDU ###
import string 
import random
if __name__ == "__main__": #main function 
    s1= string.ascii_lowercase #creating a string variable containing lowercase characters
    s2=string.ascii_uppercase #creating a string variable containing uppercase characters
    s3=string.digits #creating a string variable containing digits
    s4=string.punctuation #creating a string variable containing p
while True:
    stringset = input("Enter password length \n")
    try:
        number = int(stringset)
    except ValueError:
        print("Not a number")
    else:
        if len(stringset) >= 0 and len(stringset) <= 9:
            break
        else:
            print("Re-enter number")  
s=[] #makes an empty list
s.extend(list(s1)) #converts string s1 to list then extends at the end of the empty list
s.extend(list(s2)) #method of concatenate 
s.extend(list(s3)) # converts string s3 to list then extends at the end of the empty list
s.extend(list(s4)) #converts string s4 to list then extends at the end of the empty list
random.shuffle(s) #this will shuffle the list containing all upercase characters ,lowercase characters, digits and punctuation
print("Your Password is: ") 
print("".join(s[0:number])) #THIS LINE WILL PRINT THE PASSWORD


    

