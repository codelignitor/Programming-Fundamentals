## IMPORTS GO HERE IF REQUIRED
import os

## END OF IMPORTS


### YOUR CODE FOR writeMissingEntries FUNCTION GOES HERE ###
def writeMissingEntries(line):
    #for l in line:
    try:
        if len(line) <5:
            sum=line
            print(line)
            
            
    except IndexError:
        print("Index out of range ")

rows=[]
with open (filename, 'r') as f:
    for line in f:
        
        rows.append(line.strip().split(','))
for l in rows:
    

    writeMissingEntries(l)


with open("logfile.log", 'w') as f: 
    for l in rows: 
        out_line = writeMissingEntries(l)  # and then save this to a file 
        result = ','.join(l)
        f.write(result + "\n")

#### End OF MARKER







if __name__ == '__main__':
    
    #data = ['18P-0006,Ahmed Khan,1,8','18P-0130,Ali Hassan,A,2,4','18P-6061,Ikram Durrani,12,4','18P-6089,Muhammad,14','18P-6154,Syed Shahid Khaqani,1,2,3','18P-6064,Hamza Arif,6.5,7,2.5','18P-6065,MuhammadAli,2,3.2,4']

    #writeMissingEntries(data)

    """
    # output of logfile.log:
    #[18P-0006,Ahmed Khan,1,8]
    #[18P-0006,Ahmed Khan,1,8]
    #[18P-6061,Ikram Durrani,12,4]
    #[18P-6089,Muhammad,14]

    """
