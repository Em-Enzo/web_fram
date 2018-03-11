# Written by Em-Enzo
# atm money pull 
# 
# allowed papers: 100, 50, 10, 5, and rest of request

money = 500 # monny existes 

request = 277 # mount requested 



def money_pull(money, request):
	if(request>money):
    		request = money
	if(request<=0):
    		print"Please enter right request"
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


money_pull(money, request)




	