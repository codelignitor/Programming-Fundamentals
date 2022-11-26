## IMPORTS GO HERE if required

## END OF IMPORTS 


#### YOUR CODE FOR jobOffer GOES HERE ####

def jobOffer(salary,location="Lahore"):
	if salary> 40000 and location=="Peshawar":
		return ("I’ll take it!")
	elif salary<100000 and location=="Karachi":
		return("No way")
	elif salary>=100000 and location=="Karachi":
		return("I’ll take it!")
	elif salary>= 60000 :
		return("I’ll take it!")
	else:
		return("No thanks, I can find something better.")


#### End OF MARKER
