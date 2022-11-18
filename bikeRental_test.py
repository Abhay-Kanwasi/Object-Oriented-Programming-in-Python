import unittest
from datetime import datetime, timedelta
from bikeRental import BikeRental,Customer

class BikeRentalTest(unittest.TestCase):

    def test_Bike_Rental_displays_current_stock(self):

        shop1 = BikeRental()
        shop2 = BikeRental(10)
        self.assertEqual(shop1.displaystock(),0)
        self.assertEqual(shop2.displaystock(),10)
    
    # Test cases for hourly basis 

    def test_rentBikeOnHourlyBasis_for_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnHourlyBasis(-1),None)

    def test_rentBikeOnHourlyBasis_for_zero_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnHourlyBasis(0),None)
    
    def test_rentBikeOnHourlyBasis_for_valid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentBikeOnHourlyBasis(2).hour, hour)

    def test_rentBikeOnHourlyBasis_for_invalid_positive_number_of_bikes(self):
        shop = BikeRental()
        self.assertEqual(shop.rentBikeOnHourlyBasis(11),None)



    # Test cases for daily basis

    def test_rentBikeOnDailyBasis_for_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnDailyBasis(-1),None)

    def test_rentBikeOnDailyBasis_for_zero_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnDailyBasis(0),None)
    
    def test_rentBikeOnDailyBasis_for_valid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentBikeOnDailyBasis(2).hour, hour)

    def test_rentBikeOnDailyBasiss_for_invalid_positive_number_of_bikes(self):
        shop = BikeRental()
        self.assertEqual(shop.rentBikeOnDailyBasis(11),None)
    
    
    # Test cases for weekly basis
    def test_rentBikeOnWeeklyBasis_for_negative_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnWeeklyBasis(-1),None)

    def test_rentBikeOnWeeklyBasis_for_zero_number_of_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentBikeOnWeeklyBasis(0),None)
    
    def test_rentBikeOnWeeklyBasis_for_valid_positive_number_of_bikes(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentBikeOnWeeklyBasis(2).hour, hour)

    def test_rentBikeOnWeeklyBasis_for_invalid_positive_number_of_bikes(self):
        shop = BikeRental()
        self.assertEqual(shop.rentBikeOnWeeklyBasis(11),None)

    
    def test_returnBike_for_invalid_rentalTime(self):

        # Create a shop and then create a customer
        shop = BikeRental(10)
        customer = Customer()

        # Let customer return a bike instead of renting it.
        request =   customer.returnBike()
        self.assertIsNone(shop.returnBike(request))

        # manually check return funciton with error values.
        self.assertIsNone(shop.returnBike((0,0,0)))
    
    def test_returnBike_for_invalid_rentalBasis(self):
        shop = BikeRental()
        customer = Customer()

        customer.rentalTime = datetime.now()
        customer.bikes = 3

        customer.rentalBasis = 7

        request = customer.returnBike()
        self.assertEqual(shop.returnBike(request),0)
    
    def test_returnBike_for_invalid_numberOfBikes(self):
        shop = BikeRental(10)
        customer = Customer()
        
        # create a valid runtime and rentbasis
        customer.rentalTime = datetime.now()
        customer.rentalBasis = 1

        #create invalid bikes
        customer.bikes = 0

        request = customer.returnBike()
        self.assertIsNone(shop.returnBike(request))
    
    def test_bike_for_valid_crediantials(self):

        # Create a shop and customers
        shop = BikeRental(50)
        customer1 = Customer()
        customer2 = Customer()
        customer3 = Customer()
        customer4 = Customer()
        customer5 = Customer()
        customer6 = Customer()

        # Valid rental basis for each customers
        customer1.rentalBasis = 1
        customer2.rentalBasis = 1
        customer3.rentalBasis = 2
        customer4.rentalBasis = 2
        customer5.rentalBasis = 3
        customer6.rentalBasis = 3

        # Valid bikes for each customer
        customer1.bikes = 1
        customer2.bikes = 5
        customer3.bikes = 2
        customer4.bikes = 8
        customer5.bikes = 15
        customer6.bikes = 30

        # Past valid rental times for each customer
        customer1.rentalTime = datetime.now() + timedelta(hours=-4)
        customer1.rentalTime = datetime.now() + timedelta(hours=-23)
        customer1.rentalTime = datetime.now() + timedelta(hours=-4)
        customer1.rentalTime = datetime.now() + timedelta(hours=-13)
        customer1.rentalTime = datetime.now() + timedelta(hours=-6)
        customer1.rentalTime = datetime.now() + timedelta(hours=-12)

        # Make all customers returns their bikes
        request1 = customer1.requestBike()
        request2 = customer1.requestBike()
        request3 = customer1.requestBike()
        request4 = customer1.requestBike()
        request5 = customer1.requestBike()
        request6 = customer1.requestBike()

        # Check all customers get correct bill
        self.assertEqual(shop.returnBike(request1),20)
        self.assertEqual(shop.returnBike(request2),20)
        self.assertEqual(shop.returnBike(request3),20)
        self.assertEqual(shop.returnBike(request4),20)
        self.assertEqual(shop.returnBike(request5),20)
        self.assertEqual(shop.returnBike(request6),20)

class CustomerTest(unittest.TestCase):

    def test_return_Bike_with_valid_input(self):

        customer = Customer()

        # create valid rentalbasis and bikes
        customer.rentalBasis = 0
        customer.bikes = 0

        # created invalid rentalTime
        customer.rentalTime = 0
        self.assertEqual(customer.returnBike(),(0,0,0))

if __name__ == "__main__":
    unittest.main()





    
    