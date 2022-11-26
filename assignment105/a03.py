## IMPORTS GO HERE if required

## END OF IMPORTS 


#### YOUR CODE FOR saddle_points GOES HERE ####

def saddle_points(matrix):
    """
    A saddle point is an element which is greater than or equal to every
    element in its row and also less than or equal to every element in
	its column.
    """
    result = set()
    for idx, r in enumerate(matrix): #enumerate() method adds a counter to an iterable and returns it in a form of enumerate object
        List = [(i, items) for i, items in enumerate(r) if items == max(r)]
        for i, val in List:
            column = [r[i] for r in matrix]
            if val == min(column):
                result|= {(idx, i)}
    return result
	
#### End OF MARKER


