## IMPORTS GO HERE
## END OF IMPORTS


### YOUR CODE FOR split_safe() FUNCTION GOES HERE ###
def split_safe(s):
    for l in s:
        v = s.split(',')
        return (v)
#### End OF MARKER



### YOUR CODE FOR read_data() FUNCTION GOES HERE ###
def read_data(filename):
    with open(csv_filename, 'r') as f: 
        for line in f: 
            print (line.strip())
            print(split_safe)
#### End OF MARKER

if __name__ == '__main__':
    print(split_safe("Name,'Father Name',Address,Age"))
    print(split_safe("Ali,Tariq,'House 10, Street 20',30"))

    print(read_data('', 'file.csv'))
    pass
