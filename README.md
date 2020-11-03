# Inheritance-in-python

Q1. In an object-oriented system we can achieve the reuse of data or behavior via inheritance. That is one class (in this case the Employee class) can inherit features from another class (in this case Person). This is shown pictorially below:

 

In this diagram, the Employee class is shown as inheriting from the Person class. This means that the Employee class obtains all the data and behavior of the Person class. It is therefore as though the Employee class has defined three attributes name, age and id and two methods birthday() and calculate_pay().

a.	In this lab, task is to create a Person class with name and age attributes.Person class will have birthday() method, which will print sample output shown at the end of lab sheet. Carefully think about statements in this method’s body.

b.	You will now define the class Employee as being a class whose definition builds on (or inherits from) the class Person. Employee class will have an attribute id. In your Employee class, define a method called calculatePay(), which should be able to access the attributes name and age just as it can access the attribute id. calculatePay() method will have an input argument to define/provide the total number of working hours of an employee. calculatePay() method will use the employee’s age to determine the rate of pay to apply. If employee’s age is less than 21, their base pay rate is $7.5 per hour otherwise their pay rate will be the base pay rate + 2.50 (do not hard code this value as the base pay rate can change any time). This method should return total wage of an employee.

c.	Now define another class SalesPerson as being a class whose definition inherits from the class Employee. The class SalesPerson has a name, an age and an id as well as a region and a sales total (SalesPerson class attributes). It also has the methods birthday(), calculatePay() and bonus(). The bonus() method will multiple total sales by 0.5 to calculate and return the bonus amount received by the sales person (see sample input and output).

Sample Input:
p = Person('Kevin', 45) # Call to Person class
e = Employee('Den', 21, 7468)  # Call to Employee class	 
s = SalesPerson('Phoebe', 21, 4712, 'AUS', 30000.0) 

Sample Output:

Person # Print the word Person here to indicate you are using Person class
Kevin is 45
-------------------------
Employee
Happy birthday you were 21
You are now 22
Your Pay: 400.0
-------------------------
SalesPerson
Happy birthday you were 21
You are now 22
Your Pay: 400.0
Bonus: 15000.0



















