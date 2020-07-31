def line_break(x):
    print(str(x) + '---------' + str(x) + '---------' +
          str(x) + '---------' + str(x) + '---------')


lb = line_break

'''

~appendix
~lb(0): instance variables vs. class variables
~lb(1): [creating pay raise method universally to employees]
~lb(2): how a class variable should be used here^
~lb(3): why one can access the class variable from one's instance
~lb(4): a lil trick to get a better idea of what's going on
~lb(5): modifying the class variable outside the class via Class
~lb(7): how (self.classvariable) is more flexible than (class.classvariable) for class variable modification
~lb(8): when to (class.classvariable) vs. (self.classvariable)
~lb(9): since there such a thing as a class variable, is there also a class method?
'''

lb(0)

'''
in the previous class, you learned that instance variables are used for data that is unique to each instance,
so the instance variables were the:

-self.first = first
-self.last = last
-self.pay = pay
-self.email
that were set within the __init__() method, which are set for each instance of the employee that you create.

class variables are variables that are shared among all instances of a class.

---------------------------------------------------------
while instance variables can be unique for each instance,
class variables should be the same for each instance.
---------------------------------------------------------
'''

lb(1)
# exemplar candidate of a class variable:

# e.g. a company gives an annual raise to all its employees.
# while the amount will be different employee-to-employee, year-to-year,
# the calculation to work out the proportion increase of self.pay() will be the same to each employee
# (i.e. this should remain the same to all employee instances)

# 1) first, hardcode this outside, not as a class variable, to see why we would want it as a class variable instead:

# (referring to the Employee class made in the previous class):


class Employee:

    num_of_emps = 0    # refer to line 201
    raise_amt = 1.04  # refer to line 90

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1  # refer to line 203

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)    # refer to line 104


emp_1 = Employee('JinYoung', 'Choi', 80000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.pay)
#returns: 80000
emp_1.apply_raise()
print(emp_1.pay)
#returns: 83200

lb(2)
# the above method of creating a new class method is good,
# but when you want to e.g. change the raise amount from (1.04) to whatever amount ( ),
# it would be a hassle to scroll through the Employee Class to find the apply_raise method and amend accordingly.

# instead, if you make that number (  ) into a variable within the class (i.e. class variable!):
# and put it on top of the class (^refer to line 58!), it would be much easier to modify.

# now, when applying the class variable to the method, it needs to be defined.
# this is because when you access the class variable, you do so through a) the class itself or through b) the instance of the class:

'''
a) to access through the class itself:
def apply_raise(self):
    self.pay = int(self.pay * Employee.raise_amt) <-- 'Employee' (class) + 'raise_amt' (class variable)
or
b) access through the instance of the class:
def apply_raise(self):
    self.pay = int(self.pay * self.raise_amt) <-- 'self' (class instance) + 'raise_amt' (class variable)

^decided to follow b) (refer to line 72).'''

# ALSO, see how using b) can extend its application in lb(7)

lb(3)
# printing out a few lines to get a better idea of what's going on:

# a)
# accessing raise_amt class variable from Employee Class
print(Employee.raise_amt)
# returns 1.04

# b)
# accessing raise_amt class variable from emp_1 instance
print(emp_1.raise_amt)
# returns 1.04

# c)
# accessing raise_amt class variable from emp_1 instance
print(emp_2.raise_amt)
# returns 1.04

# when you try to access an attribute on an instance, 1) it will first check if the instance contains that attribute.
# if the instance doesn't contain that attribute,
# 2) it will see if the class (or any class that it inherits from) contains that attribute

# so when one accesses the raise_amt from instances (e.g. b) and c)),
# the instances don't actually contain the attribute themselves, but accessing the Class's attributes.

lb(4)

print(emp_1.__dict__)  # running __dict__ on the emp_1 instance
#returns: {'first': 'JinYoung', 'last': 'Choi', 'pay': 83200, 'email': 'JinYoung.Choi@company.com'}
# you can see that there is no raise_amt attribute here^.

print(Employee.__dict__)  # running __dict__ on the Employee Class
# returns: {'__module__': '__main__', 'raise_amt': 1.04, ...}
# you see that the Employee does contain the ^ raise_amt attribute.
# this is the value that the instances emp_1,emp_2 see when you access the attribute via them (instances)

lb(5)
# modifying the class variable (raise_amt) outside the class itself:

# a) modifying via Class:
# using the '(Class).(classvariable) = ' structure, raise_amt is modified to 1.05
# Employee.raise_amt = 1.05

# print(Employee.raise_amt)
# #returns: 1.05
# print(emp_1.raise_amt)
# #returns: 1.05
# print(emp_2.raise_amt)
#returns: 1.05

lb(6)
# b) modifying via instance:

# using the '(instance).(classvariable) = ' structure, raise_amt is modified to 1.05, specifically for emp_1!
emp_1.raise_amt = 1.05
print(Employee.raise_amt)
# returns: 1.04 <-- i.e. Class variable did not change!
print(emp_1.raise_amt)
# returns: 1.05 <-- i.e. class variable changed for emp_1 instance!
print(emp_2.raise_amt)
# returns: 1.04 <-- i.e. class variable did not change for emp_2 instance.

# when you made the 'emp_1.raise_amt = 1.05' assignment, it created the raise_amt attribute within the emp_1 instance.
print(emp_1.__dict__)
#returns: {'first': 'JinYoung', 'last': 'Choi', 'pay': 83200, 'email': 'JinYoung.Choi@company.com', 'raise_amt': 1.05}

# now emp_1 has the 'raise_amt': 1.05 value within the instance itself.
# which means that emp_1 will find the attribute within itself first (and will successfully find it)
# before proceeding to find it within the Employee Class it inherits from.
# hence, emp_1 will show a 1.05 raise_amt instead of the 1.04 raise_amt that is generally applied to the Employee Class.

lb(7)
# now, with lb(6) in mind, when applying the class variable to the class method,
'''
it is much better to go apply the class variable specific to the instance:
...
self.pay = int(self.pay * self.raise_amt)

than to apply the class variable specific to the class:
...
self.pay = int(self.pay * Employee.raise_amt)

This is because the former will allow you to tweak the class variable specifically to the instance (as with the case of emp_1),
whereas the latter will make the class variable un-modifiable to each instance.

n.b. also, using the former will allow any subclass* to override that constant if they wanted to.
*subclasses will be looked at in the later classes'''

lb(8)
# now, to consider another example where it wouldn't make sense to use (self.classvariable) like in lb(7)

# e.g. you want to keep track of how many employees you have.
# the number of employees should be the same for all instances of the class.
# creating the num_of_emps class variable and setting it to 0 for now (refer to line 57)

# each time you create an emp, the num_of_emps is to increment by 1. (refer to line 66)
# you can do that within the .__init__() method since the method runs everytime you create an employee.

# within the .__init__() method, you access the class variable through the Class*
# which is why number_of_emps is accessed by 'Employee.number_of_emps' instead of 'self.number_of_emps'.
# to reiterate, you only access the class variable through the class, and not the instance.

#*class variable is accessed through the Class and not instance,
# because whereas in the previous example of (raise_amt) class variable, it's nice to have a constant class value (1.04)
# that can be OVERRIDDEN per instance (i.e. case with emp_1) if you really need it to be.

# but in this case of (num_of_emps) class variable, there is no use case one can think of,
# where you would want the total number of employees to be different for any one instance.

print(Employee.num_of_emps)  # refer to line 227
# returns 2

emp_3 = Employee('Stacy', 'Jackson', 70000)
emp_4 = Employee('John', 'Appleseed', 120000)

print(Employee.num_of_emps)
# returns 4

# num_of_emps was incremented four times when you instanciated the emp_1 and emp_2 earlier, and emp_3 and emp_4 instances above.

# when the print (Employee.num_of_emps) is executed before instanciating emp_3 and emp_4, (refer to line 216),
# the returned num_of_emps is 2, since the total number of employees prior to adding emp_3 and emp_4 was 2 (from emp_1 and emp_2)

lb(9)
# now, if there is a class variable, is there a class method?
# yes. this will be explored in the next class.
