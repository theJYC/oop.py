def line_break(x):
    print(str(x) + '---------' + str(x) + '---------' +
          str(x) + '---------' + str(x) + '---------')


lb = line_break

'''

~appendix
~lb(0): putting class into context
~lb(1): difference between a class and an instance of that class
~lb(2): instance variables
~lb(3): initialising class attributes
~lb(4) - lb(5): creating methods
~lb(6): common mistake (forgetting the (self) arg when creating a method)
'''

# classes allow us to logically group our data/functions in a way that is easy to reuse and easy to build-upon if need be.

# data and functions that are associated with a specific class are called attributes and methods.
# method = function that is associated with a class

'''
if you had an application for your company, and you wanted to represent your employees in your python code:
this would be a great use case for a class since each indiv. employee will have specific attributes and methods.
e.g. each employee will have a name, email address, pay, actions they can perform.
a class would provide a blueprint to create each employee, so you wouldn't have to do this manually each time from scratch.
'''
lb(0)
# making a class called Employee


class Employee:
    pass  # if you ever need to leave a class empty, simply put in 'pass' and python will leave it for now


lb(1)
# difference between a class and an instance of a class
# your class is basically a blue print for creating instances.
# and each employee that is created from the class Employee will be an instance of that class.

emp_1 = Employee()  # one instance
emp_2 = Employee()  # another instance

# each of these^ will be their own unique instances of the Employee class.

print(emp_1)
# returns: <__main__.Employee object at 0x7fbb0606c700>
print(emp_2)
# returns: <__main__.Employee object at 0x7fbb0606c340>

#^they're unique because they both have different locations here in memory.

lb(2)
# instance variables contain data that is unique to each instance.
# you could manually create instance variables for each employee as below:

emp_1.first = 'JinYoung'
emp_1.last = 'Choi'
emp_1.email = 'JinYoung.Choi@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000

print(emp_1.email)
# returns: JinYoung.Choi@company.com
print(emp_2.email)
# returns: Test.User@company.com

# now, you wouldn't want to manually set these everytime. It's a lot of code and its also prone to mistakes.

lb(3)
# to set all of this information automatically for each employee when they're created,
# use the special __init__() method inside the class. 'init' for 'initialise'

# when you create a method within a class, it receives the instance as the first argument automatically.
# by convention, you call the instance 'self'.
# after self, you specify what other arguments you want to accept


class Employee:
    def __init__(self, first, last, pay):
        # these arguments (first, last, pay) are called instance variables
        self.first = first
        self.last = last
        self.pay = pay
        # we can create the email here using the first and the last name
        self.email = first + '.' + last + '@company.com'

    def fullname(self):  # refer to line 144
        return f'{self.first} {self.last}'


# when we set self.first = first,
# that's essentially the same thing as emp_1.first = 'JinYoung'.
# though now, instead of doing this manually, it will be done automatically when you create your employee object.



# now you can put in the values you specified in the __init__ method:
emp_1 = Employee('JinYoung', 'Choi', 80000)
emp_2 = Employee('Test', 'User', 60000)

'''
when emp_1 is created, the __init__ method is run automatically:
class Employee:
    def __init__(self, first, last, pay)

whereby:
-self = emp_1
-first = 'JinYoung'
-last = 'Choi'
-pay = 80000
'''

print(emp_1.email)
# returns: JinYoung.Choi@company.com
print(emp_2.email)
# returns: Test.User@company.com

lb(4)
# first, last, pay, and email are all attributes of our Employee class.
# if you wanted the ability to perform some kind of action,
# to do that you can add some methods to your class.

# e.g. to be able to display the full name of an employee--

# a) you could do it manually by printing a formatted string:

print(f'{emp_1.first} {emp_1.last}')
# returns: JinYoung Choi

# now this would be quite a lot to have to write each time.

# so instead you can put create a method within the class,
# that allows you to put this functionality in one place--

# b) creating a method (that prints the fullname of emp_):

# refer to lines 94,95.

print(emp_1.fullname())
# returns: JinYoung Choi

lb(5)
# lastly, you can also run this method (e.g. .fullname()),
# using the class name itself, which makes it a bit more obvious of what's going on in the background

# when you run the method from the class, you have to manually pass in the instance in the argument.
Employee.fullname(emp_1)  # <-- note the emp_1, which is the instance!

# to sum, here are two lines of code:
# 1) calling the method on the instance (emp_1)
emp_1.fullname()  # don't need to pass in self; it does it automatically

# 2) calling the method on the Class:
# do need to pass in instance; doesn't know what instance you want to run the method with
Employee.fullname(emp_1)

# now:

print(emp_1.fullname())
# JinYoung Choi
print(Employee.fullname(emp_1))
# JinYoung Choi

lb(6)
# when creating a method in a class, be sure to always include the (self) argument!:

# i.e. instead of writing:

'''
a)
def fullname():
    return 'xyz'

WRITE INSTEAD:

b)
def fullname(self):
    return 'xyz'


if a) is done, when trying to use the method outside the class,
i.e. print(emp_0.fullname()), it will throw a TypeError: fullname() takes 0 positional argument but 1 was given

the instance (emp_0) is being passed automatically, so the instance arg should be expected within the creation of the method!
'''
