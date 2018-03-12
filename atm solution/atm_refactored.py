# Written by Em-Enzo
# atm money pull 
# 
# allowed papers: 100, 50, 10, 5, and rest of request



class ATM():
    """docstring for ATM"""
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name 
        self.withdrawals_list = []
    
    def withdraw(self, request):
        """ Push the money to the client """
        print ("Welcome to "+self.bank_name)
        print ("current balance is :: "+str(self.balance))
        print ("="*30)
        if(request>self.balance):
                print ("It seems like you have a fotrune sir, I'am affraid i can't afford that!!")
                print ("="*30)                
        elif(request<=0):
                print"Please enter right request"
        else:
            self.withdrawals_list.append(request)
            self.balance -= request
            self.process_request(request)
        print ("="*30)
        return self.balance 


    @staticmethod
    def process_request(request):
        """ Process the operation """
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
                   

    def show_withdrawals(self):
        """ print the history of withdrawals """
        for withdrawal in self.withdrawals_list:
            print("Your withdrawal list ::"+str(withdrawal))




balance1 = 500 # monny existes 
balance2 = 1000

atm1= ATM(balance1, "Smart Bank")
atm2= ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(800)

atm1.show_withdrawals()

atm2.withdraw(100)
atm1.withdraw(2000)

atm2.show_withdrawals()



	