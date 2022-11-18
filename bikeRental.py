import datetime

# This BikeRental class will handle all the internal mechanism of this Bike rental system.
class BikeRental:

    def __init__(self,stock = 0):
        self.stock = stock
    
    def displaystock(self):
        print("We have currently {} bikes available to rent.".format(self.stock))
        return self.stock
    
    def rentBikeOnHourlyBasis(self,n):
        if n<=0:
            print("Number of bikes should be positive.")
            return None
        elif n>self.stock:
            print("Sorry we have currently {} bikes available to rent".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented a {} bike on hourly basis today at {} hours.".format(n,now.hour))
            print("You will be charged 5 Rupees per hour as per bike.")
            print("We hope that you will enjoy our sevices.")

            self.stock -= n
            return now
        
    def rentBikeOnDailyBasis(self,n):
        if n<=0:
            print("Number of bikes should be positive.")
            return None
        elif n> self.stock:
            print("Sorry! We currently have {} bikes for rent".format(n,now.hour))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented a {} bike on hourly basis today at {} hours.".format(n,now.hour))
            print("You will be charged 20 Rupees per hour as per bike.")
            print("We hope that you will enjoy our sevices.")

            self.stock -= n
            return now
    
    def rentBikeOnWeeklyBasis(self,n):
        if n<=0:
            print("Number of bikes should be positive.")
            return None
        elif n>self.stock:
            print("Sorry! We currently have {} bikes for rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented a {} bike on hourly basis today at {} hours.".format(n,now.hour))
            print("You will be charged 60 Rupees per hour as per bike.")
            print("We hope that you will enjoy our sevices.")

            self.stock -= n
            return now
    
    def returnBike(self,request):
        rentalTime,rentalBasis,numOfBikes = request
        bill = 0
        if rentalBasis and rentalTime and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            # Hourly bill calculation of rent.
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds/3600) * 5 * numOfBikes
            
            # Daily bill calculation of rent.
            if rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes
            
            # Weekly bill calculation of rent.
            if rentalBasis == 3:
                bill = round(rentalPeriod.days/7) * 60 * numOfBikes
            
            if(3<=numOfBikes<=5):
                print("You are eligible for family rental prmotion of 30% dissount")
                bill = bill * 0.7
            
            print("Thanks for returning your bike. Hope you enjoyed our services...")
            print("Your Bill : {}".format(bill))
            return bill
        else:
            print("Are you sure?\nYou rented any bike from us.")
            return None

# This Custoemr class will handle all the customer requests and return details 
class Customer:

    def __init__(self):
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0
    
    def requestBike(self):
        bikes = input("How many bikes would you like to rent : ")
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        if bikes < 1:
            print("Invalid input.\nNumber of bikes must be greater than zero.")
            return -1
        else:
            self.bikes = bikes
        return self.bikes
    
    def returnBike(self):
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalBasis, self.rentalTime, self.bikes
        else:
            return 0,0,0

