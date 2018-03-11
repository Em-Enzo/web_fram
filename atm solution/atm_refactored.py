# Written by Em-Enzo
# atm money pull 
# 
# allowed papers: 100, 50, 10, 5, and rest of request



balance = 500 # monny existes 


def withdraw(balance, request):

	print ("current balance is :: "+str(balance))
	if(request>balance):
    		print ("It seems like you have a fotrune sir, I'am affraid i can't afford that!!")
    		return -1
	if(request<=0):
    		print"Please enter right request"
	else:
		balance -= request
		while request>0:
    			if(request>=100 ):
        			print "give 100"
        			request=request-100
    			elif(request>=50):
            			print "give 50"
            			request=request-50
    			elif(request>=10):
                			print "give 10"
                			request=request-10
    			elif(request>=5 ):
            		        	print "give 5"
                		    	request=request-5
    			else:
                	    	 	print "give "+str(request)
                    		 	request=0
   		return balance

balance= withdraw(balance, 277)
balance= withdraw(balance, 30)
balance= withdraw(balance, 5)
balance= withdraw(balance, 500)


	