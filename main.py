import string 
import random
if __name__ == "__main__":
    s1= string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
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
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
print("Your Password is: ")
print("".join(s[0:number]))


    

