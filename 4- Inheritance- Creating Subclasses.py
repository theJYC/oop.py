def line_break(x):
    print(str(x) + '---------' + str(x) + '---------' +
          str(x) + '---------' + str(x) + '---------')


lb = line_break

'''

~appendix
~lb(0): intro. to inheritance, classes and subclasses
~lb(1): creating a subclass
~lb(2): help() function and method resolution order
~lb(3): how to modify a parent-class attribute specifically for the subclass
~lb(4): Keeping your code DRY: Keep It Simple Super().__init__()! <KISS>
~lb(5): subclass specific argument (prog_lang)
~lb(6): isinstance(inst, cls) and issubclass(subcls, cls) built-in functions

'''

lb(0)
# just as it sounds, inheritance allows you to inherit attributes and methods from your parent class.
# this is useful because you can create subclasses and inherit all of the functionalities of the parent class,
# and then overwrite or add completely new functionality without affecting the parent class in any way

# e.g. so far along the OOP journey, you have been working with the below Employee class:

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):  # refer to line A

    raise_amt = 1.10  # refer to line B

    def __init__(self, first, last, pay, prog_lang):  # refer to line C
        super().__init__(first, last, pay)  # refer to line D
        self.prog_lang = prog_lang   # refer to line E


# let's say you wanted to get a little more specific here and create different types of employees-
#-e.g. create Developers and Managers. these would be great candidates for subclasses,
# because both Developers and Managers are going to have names, email addresses, and salaries,
# and those are all things that the Employee class already has.

# so instead of copying all this code into your Developer and Manager subclasses,
# you can just reuse that code by inheriting from Employee class.


lb(1)
# to create a subclass,
# create the class and pass in as argument what specific classes you want this subclass to inherit from (refer to line A)

# right now, even without any code of its own,
# the subclass Developer will have all of the attributes and methods of the Employee class.

dev_1 = Developer('JinYoung', 'Choi', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 90000, 'JavaScript')

print(dev_1.email)
#returns: JinYoung.Choi@email.com
print(dev_2.email)
#returns: Test.Employee@email.com

# when you instantiated dev_1 and dev_2, it first looked at the Developer class to look for the __init__() method.
# it's not going to find it within the Developer subclass since it's currently empty.
# what python will do is then walk up this 'chain' of inheritance until it finds what it's looking for.
# this 'chain' is called the method resolution order.

lb(2)
# the help function makes these things a lot easier to visualise.

help(Developer)
'''returns (selected only upto the <method resolution order> part. see lb(2) in print for more)

class Developer(Employee)
 |  Developer(first, last, pay)
 |
 |  Method resolution order:
 |      Developer
 |      Employee
 |      builtins.object

'''
# method resolution order is one of the first things that get printed out.
# this is the list of places python searches for attributes and methods.
# i.e. it first looked at the Developer class for the __init__() method, and when it didn't find it there,
# it then went up to the Employee class and found it there so that's where __init__() method was executed it.

# if it had not found it in the Employee class, the last place it would have looked is the base Objects class (builtins.object).
# every class in python inherits from this base object.

lb(3)
# now, let's say you wanted to customise your Developer subclass a little:
# making a very simple one line change: to change the raise_amt attribute from the Employee class.

# what happens when you apply a raise on a developer:
print(dev_1.pay)
#returns: 50000
dev_1.apply_raise()
print(dev_1.pay)
#returns: 52000

# so the above shows that dev_1 was given a raise with the raise_amt of 1.04 (4%) set in Employee class.
# but let's say that you wanted to give Developers a raise_amt of 1.10 (10%) instead of the Employee raise_amt.

# to make this change, it's just as easy as accessing the Developer subclass and setting the raise_amt as so (refer to line B)
print(dev_1.pay)
#returns: 55000

# now dev_1 is applied the Developer raise_amt of 10% instead of the Employee raise_amt of 4%.

# n.b. changing the raise_amt in the Developer subclass did not have any impact on the raise_amt of the Employee class
# e.g. here is an Employee (note: not Developer) with the same salary (50000)
emp_1 = Employee('JinYoung', 'Choi', 50000)
emp_1.apply_raise()
print(emp_1.pay)
#returns: 52000

# given that emp_1 was created with the Employee class (and not Developer subclass), it still has the raise_amt of 1.04 (or 4%).
# i.e. you can make changes to the subclasses without worrying breaking anything in the parent class.

lb(4)
# now for some more complicated changes to the subclass...
# sometimes you want to initiate the subclasses with more info. than their parent class can handle.

# e.g. for dev_3, you want to also pass in their main programming language as their attribute,
# but currently the Employee class only accepts first/last name and pay.

# a way to go around this is to give the Developer subclass its own __init__ method.
# copy and paste the def __init__() from the Employee class into the Developer subclass
# along with the existing args, also add 'prog_lang' for main programming language (refer to line C).

# what you might be tempted to do here is to go up to the Employee class's __init__() method,
# and copy & paste the code into the Developer subclass's __init__() method.
# but you DON'T want to do that because you want to keep the code DRY and not repeat this logic in multiple places.

# instead of copy&pasting, let the Employee class's __init__() method handle the first/last name and pay arguments,
# and let the Developer subclass's __init__() method to set the prog_lang arg.

# in order to let Employee class handle first/last name and pay, write super().__init__() and pass those in as args (see line D)
# super().__init__(first, last, pay) is going to pass first, last, and pay into your Employee class's __init__() method,
# and let that class handle those arguments.

# instead of super().__init__(first,last,pay), you can write Employee.__init__(self, first, last, pay),
# although the former is preferred since it is more maintainable, esp. when multiple inheritance comes into play.
# mnemonic to remember using super().__init__() ; Keep It Simple Super().__init__()!

lb(5)
# now, you can let Developer subclass handle the 'prog_lang' argument just as you would in any other class (refer to line E)
print(dev_1.email)
#returns: JinYoung.Choi@email.com
print(dev_1.prog_lang)
#returns: Python

# as you can see, the email method came from Employee class, whereby the prog_lang arg specifically came from Developer subclass
# just by adding in the <class Developer(Employee):> line,
# you do not have to write repetetive code within the Developer subclass given the simplicity brought by inheritance.

lb(6)
# finally, python has these two built-in functions called isinstance() and issubclass().

# isinstance() will tell you if an object is an instance of a class.
# e.g. is dev_1 an instance of the Developer class?
print(isinstance(dev_1, Developer))
#returns: True

# now if you want to see if dev_1 is an instance of Employee:
print(isinstance(dev_1, Employee))
#returns: True


# issubclass will tell you if a class is a subclass of another:
print(issubclass(Developer, Employee))
# returns True

print(issubclass(Employee, Developer))
#returns False

#^since Developer is a subclass of Employee, not the other way round.
