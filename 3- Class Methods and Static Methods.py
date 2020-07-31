def line_break(x):
    print(str(x) + '---------' + str(x) + '---------' +
          str(x) + '---------' + str(x) + '---------')


lb = line_break

'''

~appendix
~lb(0): microsoftlearning's summary on the mechanics of instance/class/static methods
~lb(1): brief summary on the logic behind use of instance/class/static methods
~lb(2): @classmethod and cls
~lb(3): impact of classmethod vs regular (instance) method
~lb(4): classmethods as alternative constructors
~lb(5): staticmethods

'''

lb(0)
# excerpt from microsoftlearning notes:

# say you have a class named D and you define a regular method [inst_method(self, x, y)] within:


class D:
    def inst_method(self, x, y):
        pass

    @staticmethod  # refer to line
    def static_method(x, y):  # does not pass in the
        pass

    @classmethod  # refer to line
    def cls_method(cls, x, y):  # refer to line
        pass


# D.inst_method(1, 2)  # <-- transform to inst_method(d, 1, 2)
# D.static_method(1, 2)  # <-- no automatic transform;
# D.cls_method(1, 2)  # <-- transform to cls_method(type(d), 1, 2)
# D.cls_method(1, 2)  # <-- transform to cls_method(D, 1, 2)

lb(1)

# brief sum. of the difference between an instance/class/static methods.

# so far you have focused on instance methods, which calls the instance as the first argument (i.e. <self>),
# i.e. you used the instance method when you want to modify the instance!
# meanwhile class methods are used when a method is not really about an instance of a class, but the class itself.
# i.e. you use the classmethod when you want to modify the class (and, by default, the instances within)
# lastly, a static method is used just like a regular/freeform function that is outside a particular class,
# and static methods even behave like regular functions in that they don't implicitly pass in anything like <self> or <cls>,
# but staticmethods are just labelled as such and placed within the class given their apparent connection to the class
# i.e. you use a staticmethod just like a regular function, but a staticmethod is grouped within the class.

# lastly, class methods are good to use for alternative constructors.
# see: (https://www.geeksforgeeks.org/class-method-vs-static-method-python/)

lb(2)
# as opposed to the regular, instance method,
# a class method requires a decorator on top: @classmethod, and pass in cls as first arg (compare w/ <self> of before)
# refer to line A

# using the Employee Class from previous class
class Employee:

    num_of_emps = 0
    raise_amt = 1.04  # refer to line

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod  # refer to line A
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount  # refer to line

    @classmethod  # refer to line Z
    def from_string(cls, emp_str):  # refer to line Q
        # this was step one of creating employee manually
        first, last, pay = emp_str.split('-')
        # this is step two, with Employee replaced with cls (since this is a classmethod)
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() >= 5:
            return False
        else:
            return True


emp_1 = Employee('JinYoung', 'Choi', 80000)
emp_2 = Employee('Test', 'User', 60000)

# in a nutshell, a decorator (e.g. @classmethod) is altering the functionality of your method.
# n.b. by convention, you write cls as the arg just like you'd write self as the arg for a regular method.
# n.b.b. you should NOT write 'class' instead of 'cls', since 'class' carries a different functionality in Python syntax,
# i.e. 'class' is used when you're CREATING a class in python (i.e. class Employee: ... ...).

lb(3)
# to illustrate what is meant by a method working with a class instead of a method,
# set the raise_amt class variable equal to the amount arg you're accepting from this method (refer to line ).

# class variable <raise_amt> accessed through class <Employee>
print(Employee.raise_amt)
# returns: 1.04
# class variable <raise_amt> accessed through instance <emp_1>
print(emp_1.raise_amt)
# returns: 1.04
# class variable <raise_amt> accessed through instance <emp_2>
print(emp_2.raise_amt)
# returns: 1.04

# all of these are equal to 1.04 since the raise_amt class variable is set to 1.04 (refer to line 64).
# if you wanted to change this from 1.04 to 1.05,

# use the set_raise_amt class method!
# noting that def set_raise_amt(cls, amount) requires two positional args (cls, amount) and it automatically accepts the class
# so just pass in the amount
Employee.set_raise_amt(1.05)

# now, to confirm whether this class method indeed changed the class variable to 1.05:

print(Employee.raise_amt)
# returns: 1.05
print(emp_1.raise_amt)
# returns: 1.05
print(emp_2.raise_amt)
# returns: 1.05


lb(4)
# you can use classmethods in order to provide multiple ways of creating your objects.

# e.g. someone is using the Employee class, whereby they have employee info. in the form of a string separated by hyphens,
# so they constantly need to first parse the strings before creating new employees.
# so is there a way to just pass in a string and create an employee from that?

# YES!

# to illustrate, here is the situation:

# this inquierer has three strings that each hold employee info. (i.e. info. that are otherwise a good match for Employee class)
emp_str_1 = 'JaeIn-Moon-70000'
emp_str_2 = 'Donald-Trump-300000'
emp_str_3 = 'Winston-Churchill-270000'

# as one can note, each of the strings above follow this general format (referring to Employee class):
emp_str_n = 'first-last-pay'

# if you were to actually create an employee out of these strings, you'd have to 1) split based on the hyphens:
first, last, pay = emp_str_1.split('-')

# and then create a new employee by passing in those values in Employee() (which would run the __init__() method):
new_emp_1 = Employee(first, last, pay)

# so when you run it, you can see that the above steps actually worked:
print(new_emp_1.email)
#returns: JaeIn.Moon@company.com

# now, if this is a common use case, whereby the person would have to parse the strings every time to create a new employee,
# they would be better off by creating an alternative constructor that will let them pass in the string,
# and the alternative constructor will create the employee for them.

# refer to line Z

# usually alternative constructors will start with a 'from', that's just a good convention to follow (refer to line Q)

# now, instead of the above manual steps, all you have to do is to call the from_string() classmethod
# which you just created as an alternative constructor
#(note: variable to store the return of classmethod named with '_ac' to illustrate the same returned results):
new_emp_1_ac = Employee.from_string(emp_str_1)
print(new_emp_1_ac.email)
# returns: JaeIn.Moon@company.com

# now this is what is meant by 'using classmethods as alternative constructors'


lb(5)
# a lot of people get classmethods and static methods confused.
# when working with classes, regular methods automatically pass the instance as the first argument (self),
# and classmethods automatically pass the class as the first argument (cls).

# now, staticmethods don't pass anything automatically.
# so really, they just behave just like free-form functions,
# except that you include them in your classes because they have some logical connection with the class.

# let's say you wanted a simple function that would take in a date,
# and return whether or not that was a workday.

# now that has a logical connection to the Employee class,
# but it doesn't actually depend on any specific instance or class variable.
# so, instead, make this function into a staticmethod
# refer to line H

# basically this staticmethod was created with python's .weekday() method in mind, whereby
# dates where monday  == 0 and sunday == 6,
# so day.weekday >= 5 would mean saturday and sunday (the only two non-work day)
# so, the if statement was created to return False for sat and sun, and True for else.

# n.b. a good giveaway on whether a method should be a static method or not,
# is if you don't access self (i.e. instance) or cls (i.e. class) anywhere within the function.

# to test whether the staticmethod that you created is working:
import datetime
# knowing this is a sunday, i.e. not a workday
my_date = datetime.date(2020, 7, 26)

# note that you still need to call the Employee class when using staticmethod since it belongs within it
print(Employee.is_workday(my_date))
# returns False
