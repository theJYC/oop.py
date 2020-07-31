def line_break(x):
    print(str(x) + '---------' + str(x) + '---------' +
          str(x) + '---------' + str(x) + '---------')


lb = line_break

'''

~appendix
~lb(0): intro. to special methods
~lb(1): dunder? what is that?
~lb(2): dunder repr // dunder str for debugging
~lb(3): defining the dunder repr
~lb(4): defining the dunder str
~lb(5): what's going on in the background when you call repr() or str()
~lb(6): a few more special methods (arithmetic)
~lb(7): creating special dunder methods within the class to customise its functionality
~lb(8): creating special dunder methods continued.

'''
#_________________________________from previous OOP notes (+ modification)__________________________

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

    def __repr__(self):  # refer to line A
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)  # refer to line B

    def __str__(self):  # refer to line C
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):  # refer to line D
        return self.pay + other.pay

    def __len__(self):  # refer to line E
        return len(self.fullname())


emp_1 = Employee('JinYoung', 'Choi', 80000)
emp_2 = Employee('Test', 'User', 60000)

#_________________________end of code imported from previous OOP notes____________________________

lb(0)
# special methods that can be used within classes are called 'magic methods'.
# these special methods allow you to emulate built-in behavior in python and are also how you implement operater overloading

# e.g. the behavior when you add two integers together is different to the behavior when you add two strings together:
print(3 + 4)
# returns: 7
print('a' + 'b')
# returns: ab

# integers 3 and 4 were added together, while the strings 'a' and 'b' were concatenated.
# i.e. depending on what objects you're working with, the addition operator has different behaviours.

# also, when you print out:
print(emp_1)
# returns: <__main__.Employee object at 0x7f816a39bb50>

# it would be nice if you change this behaviour to print out something more user-friendly.
# and that's what these special methods will allow you to do!

lb(1)
# by defining your own special methods, you will be able to change built-in behaviours and operations.
# syntax_wise, these special methods are always surrounded by double underscores ('__')
# n.b. a lot of people call these [d]ouble [u]nderscores == dunder's.
# i.e. if someone says dunder init == __init__()

# dunder init is a special method that you have already been using and are familiar with.
# it's probably one of the most common and most used special methods people use when working with classes.


lb(2)
# let's take a look at some other common special methods.
# two special methods that you should always implement are: 1) dunder repr and 2) dunder str
# these are what are implicitly called whenever you call the repr() or str() on one of our objects:

# repr(emp_1)
# str(emp_1)

# these are what are going to fix your problem of printing out the vague employee object,
# when you printed out the emp_1 object at lb(0).

# n.b. refer to an earlier video on the difference between __repr__() and __str__()
# see: https://youtu.be/5cvM-crlDvg

# in short, __repr__ is meant to be an unambiguous representation of the object,
# and should be used for debugging and logging, etc. its really meant to be seen by other developers.

#__str__ is meant to be more of a readable representation of an object,
# meant to be used as a display to the end-user.

lb(3)
# now, onto how these two methods work;
# you always want to at least have defined the __repr__() method. (refer to line A)
# because if you have defined __repr__() without having defined the __str__(),
# then if you call __str__() on the object, it will just use the __repr__() as a fallback
#(i.e. it's good to define __repr__() within the object as a minimum)

# a good rule of thumb when defining the __repr__() method is
# to try to display something that you can copy&paste into python code that'd recreate the same object.
# trying to recreate a string that you can use to recreate the object (refer to line B)

# to illustrate:
print(emp_1)
# returns: Employee('JinYoung', 'Choi', 80000)

# as you can see, now the print(emp_1) returned a string that you specified in the __repr__() method,
# instead of printing out the ambiguous <__main__.Employee object at 0x7f816a39bb50> in lb(0).

lb(4)
# now, to define the dunder str method (read: 'string')
# as stated above, dunder str is meant to be more readable to the end user,
# which makes it slightly more arbitrary than dunder repr
# but to print out this emp_1... (refer to line C)

# now if you print out the emp_1 object again,
# it should by default use the dunder str method instead:
print(emp_1)
# returns: JinYoung Choi - JinYoung.Choi@email.com

lb(5)
# you can still access repr and str specifically:
print(repr(emp_1))
# returns: Employee('JinYoung', 'Choi', 80000)

print(str(emp_1))
# returns: JinYoung Choi - JinYoung.Choi@email.com

# when you run the repr() and the str(), what's actually going on in the background is
# that it's directly calling those special methods.

# i.e. print(repr(emp_1)) is actually:
print(emp_1.__repr__())
# returns: Employee('JinYoung', 'Choi', 80000)

# and print(str(emp_1)) would be:
print(emp_1.__str__())
# returns: JinYoung Choi - JinYoung.Choi@email.com

# these two special methods allow you to change how the objects are displayed.

lb(6)
# now, unless you're writing more complicated classes,
# dunder init/repr/str will be the special methods you'll probably use most often.

# but let's go ahead and look at a few more so you can get an idea for how these work.
# there are also a lot of special methods for arithmetic.

# so, like you saw before when you added the two integers together--
print(1 + 2)

# what this is actually doing is running a special method called dunder add (__add__())
# you can actually access this directly if you use the int object and the __add__():
print(int.__add__(1, 2))
# returns: 3

# similarly, strings are using their own dunder method,
print(str.__add__('a', 'b'))
#returns: ab

lb(7)
# you can actually customise how addition works for your object by creating that dunder add method:
# e.g. let's say that with your Employee class, you wanted to calcuate total salaries just by adding emp's together

# note: this is kind of like a contrived example because if you were to make a class like that in real life,
# it'd probably be better to be explicit about what you're adding together.
# alas, just for the sake of this example, let's go ahead and see how you'd do this...

# if you wanted to combine two emp's together and have the result be their combined salaries,
# you have to create a dunder add method (refer to line D),
# passing in self and other which will be on the left and right side of the addition, respectively.
# assuming that both self and other will be emp's, return self.pay and other.pay (refer to line E)

# to see if this works--
print(emp_1 + emp_2)
#returns: 140000

# you can see that when you added these two employee objects together, it gave you their combined salaries.

# n.b. if you didn't create this specific dunder add method within the Employee class,
# it would have thrown an error saying that it doesn't know how to add emp_1 and emp_2 together.

# essentially, the custom dunder add method that you created is telling python how to add these instances together.

lb(8)
# there are all kinds of special methods for aritmetic and you can see them in the official documentation.
# let's go ahead and run through one more example of a special method.

# if you have ever used the len() function to check the length of an object, e.g.:
print(len('Big Fat Len'))
# returns:11

# now this is also using a special dunder method in the background.

print('Big Fat Len'.__len__())
# returns:11

# i.e. if you want this len() function to work on a given object, you need to create the dunder len within
# let's say that, for example, when you ran the len method for emp instances,
# you want it to return the total number of characters in their full name

# refer to line F
# now you can use the len() function on the emp_1 instance and it would do exactly as you created the dunder len method to do:
print(len(emp_1))
#returns: 13

# i.e. emp_1's name, 'JinYoungChoi' is composed of 13 characters.
