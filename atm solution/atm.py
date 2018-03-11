# Written by Em-Enzo
# atm money pull 
# 
# allowed papers: 100, 50, 10, 5, and rest of request

money = 500 # monny existes 

request = 277 # mount requested 



def money_pull(money, request):
	if (request <= 0) or (request > money):
		print "Error, reenter the mount Please!! "
		return -1
	while request > 0:
		
		while request / 100 != 0:
			print 'give '+str(100)
			request -= 100
			break
		while request / 50 != 0:
			print 'give '+str(50)
			request -= 50
			break
		while request / 10 != 0:
			print 'give '+str(10)
			request -= 10
			break
		while request / 5 != 0:
			print 'give '+str(5)
			request -= 5
			break
		while request / 2 != 0:
			print 'give '+str(2)
			request -= 2
			break
		while request / 1 != 0:
			print 'give '+str(1)
			request -= 1
			break


money_pull(money, request)




	