from bikeRental import BikeRental,Customer

# This will be the main face of our Bike Rental System
def main():
    shop = BikeRental(100)
    customer = Customer()

    while True:
        print("""
        ======= | BIKE RENTAL SHOP | =======
        1. Display available bikes
        2. Request a bike on hourly basis 5 rupees.
        3. Request a bike on daily basis 20 rupees.
        4. Request a bike on weekly basis 60 rupees.
        5. Return a bike.
        6. Exit.
        """)

        choice = input("Enter the choice : ")
        try:
            choice = int(choice)
        except ValueError:
            print("{ValueError}")
            continue

        if choice == 1:
            shop.displaystock()
        
        elif choice == 3:
            customer.rentalTime = shop.rentBikeOnDailyBasis(customer.requestBike())
            customer.rentalBasis = 2
        
        elif choice == 2:
            customer.rentalTime = shop.rentBikeOnHourlyBasis(customer.requestBike())
            customer.rentalBasis = 1
        
        elif choice == 4:
            customer.rentalTime = shop.rentBikeOnWeeklyBasis(customer.requestBike())
            customer.rentalBasis = 3
        
        elif choice == 5:
            customer.bill = shop.returnBike(customer.requestBike())
            customer.rentalBasis, customer.rentalTime,customer.bikes = 0,0,0
        
        elif choice == 6:
            break

        else:
            print("Invalid Input!\nNow try to enter the number between")
            
    print("Thank You for using the bike rental system.")

if __name__=="__main__":
    main()