# A Bike Rental System
A full fledged bike rental system implemented in Python using object oriented programming.

## Customers Services
1. See available bikes on the shop
2. Rent bikes on hourly basis $5 per hour.
3. Rent bikes on daily basis $20 per day.
4. Rent bikes on weekly basis $60 per week.
5. Family Rental, a promotion that can include from 3 to 5 Rentals (of any type) with a   discount of 30% of the total price 

<br/>

## Bike Rental Shop Functionalities
1. issue a bill when customer decides to return the bike.
2. display available inventory
3. take requests on hourly, daily and weekly basis by cross verifying stock 

Any customer requests rentals of only one type i.e hourly, monthly or weekly
Is free to chose the number of bikes he/she wants
Requested bikes should be less than available stock.

<br/>

## Test Driven Development (TDD)
1. Tests will save you time
2. Tests don’t just identify problems, they prevent them
3. Tests make your code more attractive
4. Tests help teams work together 


## Running the tests
To run the tests, run the appropriate command below (why they are different):

1. Python 2.7: py.test bikeRental_test.py
2. Python 3.4+: pytest bikeRental_test.py
Alternatively, you can tell Python to run the pytest module (allowing the same command to be used regardle ss of Python version): python -m pytest bikeRental_test.py 

<br/>
<br/>

# Conclusion 

Implement a set of classes to model this domain and logic in short a working code!

1. Add automated tests to ensure a coverage over 85%
2. Use GitHub to store and version your code
3. Apply all the recommended practices you would use in a real project
4. Add a README.md file to the root of your repository to explain: your design, the development practices you applied and how run the tests.