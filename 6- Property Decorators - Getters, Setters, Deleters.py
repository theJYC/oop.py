def line_break(x):
    print(str(x) + '---------' + str(x) + '---------' +
          str(x) + '---------' + str(x) + '---------')


lb = line_break

'''

~appendix
~lb(0): intro. to @property decorators
~lb(1): @property decorator use case
~lb(2): creating a 'getter'
~lb(3): defining a method that can behave like an attribute
~lb(4): creating a 'setter'
~lb(5): creating a 'deleter'

'''
#_________________________________from previous OOP notes (+ modification)__________________________

class Employee(object):  # refer to line Z

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # refer to line C
    def email(self):  # refer to line B
        return '{}.{}@email.com'.format(self.first, self.last)

    @property  # refer to line D
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter  # refer to line E
    def fullname(self, name):  # refer to line F
        self.first, self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('JinYoung', 'Choi')  # refer to line A
emp_1.fullname = 'Corey Schafer'
#_________________________end of code imported from previous OOP notes____________________________

# n.b. the Employee class has been stripped down a bit so that you can focus on learning these attributes
# without other code getting in the way.

# a major FYI-- @property decorator only works on new style classes.
# i.e. Employee class needs to inherit from object (refer to line Z)
# look at stackoverflow --
# https://stackoverflow.com/questions/16502133/python-property-decorator-not-working-why/16502188

lb(0)
# property decorators allow us to give your class attributes
# getter, setter and delete functionalities as you may encounter in other languages

# looking at the employee class, you may notice that the email attribute depends on the first and last name attributes.
# so when you create the emp_1 method (refer to line A),
# it comes into the dunder init method and it sets the first name, last name,
# then it sets the email to your first name . lastname @email.com

# also you have the fullname() method which prints out the current first name and last name together.
print(emp_1.first)
# returns: JinYoung
print(emp_1.email)
# returns: JinYoung.Choi@email.com
print(emp_1.fullname)
# returns: JinYoung Choi

lb(1)
# now, if you set emp_1's firstname to Jim
# emp_1.first = 'Jim'
# that would change the output of
print(emp_1.first)
# returns: Jim
print(emp_1.email)
# returns: JinYoung.Choi@email.com
print(emp_1.fullname)
# returns: Jim Choi

# you can see that while emp_1.first was indeed changed to Jim,
# emp_1.email is still set with the firstname prior to Jim (i.e. JinYoung)
# meanwhile note that the fullname() method doesn't have this problem and evidently modified emp_1.first to 'Jim'

# everytime you run the fullname() method, it comes into the def fullname(self):
# and grabs the current first name and last name.

# meanwhile email is an attribute just like first, so that, while it is set to the combination of first and last names,
# it will not grab the current first and last name attributes as a method (e.g. fullname) would.

# so what if the people who are using your Employee class says that you need to fix this?
# that they don't want to manually change their email everytime they change their first name and last name.

# they want you to make it to where it updates the email automatically when either the first/last name is changed.

lb(2)
# your first thought might be to create an email() method just as you did with fullname(),
# but the problem with that is it would break the code for everyone currently using that class.
# i.e. they would have to go through every instance of the email attribute with an email() method.

# this is usually where people from other languages (e.g. Java) would bring up the benefits of getter and setter methods.
# and thankfully you have the opportunity to use these attributes also, using the @property decorator

# now, the property decorator (i.e. 'getter') allows you to define a method but you can access it like an attribute.

# e.g. let's go ahead and pull the self.email attribute into a method, similar to a fullname method.
# borrowing the skeletone of the fullname() method (refer to line B)
# n.b. removed the email attribute from the dunder init() since it's no longer needed.

# so, right now, the email() method is similar to your fullname() method.
# each time you ran it, it would get the current first and last name,
# but you'd have to go through your code and change every email attribute call to email method call
# i.e. wherever you did emp_1.email, you would have to modify to emp_1.email() .

# in order to continue accessing email like an attribute (so that you don't have to make all the above suggested changes),
# you can just add a @property decorator above the email() method, (refer to line C).

lb(3)
# by adding the @property decorator,
# you're defining the email() as a method in your Employee class, but you're able to access it like an attribute.

# you can do this just as easily with the fullname() method aswell (refer to line D)
# note that now the bracket after the fullname is taken off:
print(emp_1.fullname)

lb(4)
# let's use the fullname() method to also illustrate when/how you can use a setter.

# e.g. you wanted the ability to say:
emp_1.fullname = 'Donald Trump'

# and that by setting the fullname, you also wanted to automatically set the first/last name and email accordingly.
# to do that, you're going to need a setter.

# this may look strange, but the name you're going to use for your setter is
#@ +  name of the property (i.e. fullname) + .setter (refer to line E).
# and, underneath the @fullname.setter, create another method with the same name (refer to line F)
# note: make sure to pass in as second argument the value you're going to set (i.e. here it is set as 'name')

# now, referring to the format of emp_1.fullname = 'Donald Trump',
# you want to set the fullname = first and last name as above^ format.
# which could be achieved by splitting the first/last name by a ' ' (space). (refer to line G)

# what happened here is that whenever you set the emp_1.fullname to 'Donald Trump',
# it came into the @fullname.setter and parsed the name (according to line E),
# and then it set emp_1's first and last name.

# since you set the first and last name with above @fullname.setter,
# even when you printed out the email,
print(emp_1.email)
#returns: Donald.Trump@email.com

# it came into the @property email and grabbed the correct values.

lb(5)
# now you can also make a deleter in the same way--
# let's say that you were to delete the full name of your employee
# and you wanted to run some kind of clean-up code.

# to do this, copy the setter and paste it in below,
# but instead of .setter, change to .deleter,
# and this is going to not going to take in any other argument than (self)
# correspondingly, replace the format constructor with e.g. a simple print('Delete Name!')
# also add:
# 1) self.first = None
# 2) self.last = None

#(refer to line H)
# so the deleter code here is what gets run whenever you delete an attribute.
# e.g.

del emp_1.fullname
# returns: Delete Name!

print(emp_1.fullname)
# returns: None None
