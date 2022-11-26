## IMPORTS GO HERE if required
import os
## END OF IMPORTS 


#### YOUR CODE FOR numbersToText function, GOES HERE ####

#dic_numbers = {}
def numbersToText(num,lang="eng"):
    for i in range(11):
        if num==i and lang=="eng":
            return  (dic_numbers[(i)][0])
        elif num==i and lang=="urd":
            return  (dic_numbers[(i)][1])
    return('Not Available')




#### End OF MARKER


dic_numbers={}
with open("numbers.txt", 'r') as f: 
    for line in f: 
        #k,v = line.strip().split(".")
        #dic_numbers[k]=v
        t=line.strip().split(".")
        t1= t[1].strip().split(",")
        dic_numbers[int(t[0])] = t1               
#Open the file and convert each line into a python dictionary using loop 
	#a. strip and then split via fullstop (.) each line and store it in a variable t. 
	#b. Now split t[1] via comma (,) and store it in a variable t1. 
	#Add t1 to dic_numbers at the index int(t[0])


num=1
lang='urd'

#print(str(num) + " in "+ lang +" : "+ str(numbersToText(num,lang)))
#output: 1 in urd : Aik


