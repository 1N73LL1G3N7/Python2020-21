"""What is Python Class And Object?
A class is a collection of objects, and an object is defined as an instance of class possessing attributes.
The object is an entity that has state and behavior. A class has all the similar attributes, like if we have a class students,
then it will only consist of students related data, such as subjects, names, attendance ratio, etc.

By using oop, we can divide our code into many sections known as classes. Each class holds a distinct purpose or usage.
For example, if we have created a class named "Books" then all the attributes it possesses should be related to books such as the number of pages,
publishing date or price, etc.
There is no limit to the number of classes we can create in a program. Also, one class can be easily accessible by another, and we can also restrict the
access of a class so other classes can not use its functions. This concept comes in handy while working on bigger projects.
All the employees are given separate tasks to work on the classes they have been assigned. And after they are done with their contribution,
the classes can be combined as a whole to form a complete project. So, now you can understand that to become a successful programmer,
you must master the concept of OOP.

Object-oriented vs. Procedure-oriented Programming
Index	 Object-oriented programming	                                           Procedure Oriented Programming
1	     Object-oriented programming is the problem-solving approach.              It is Structure oriented.
         The computation is done by using objects.                                 Procedural programming uses a list of instructions.
                                                                                   It performs the computation step by step.
2	     OOP makes development and maintenance easier.	                           When the project becomes lengthy, it is not easy to maintain the code.
3	     OOP provides a proper way for data hiding.                                Procedural programming does not provide any proper way for data binding,
         It is more secure than procedural programming.                            so it is less secure. In Procedural programming, we can access the private
         You cannot access private data from anywhere.                             data.
4	     Program is divided into objects	                                       The program is divided into functions.

Defining a Class in Python
As in function, definitions begin with the keyword def, class begins with a class keyword.

class MyClass:
    '''This is a docstring.'''
    pass

A class is a blueprint from which objects are created. Creating a new class creates a new type of object which allows the new instances of that type to be made.
Each class instance has attributes attached so that it could maintain its state. Class instances can also have methods that are defined by its class for
modifying its state.

Suppose we have to create a program that requires the data of all the individuals in a school. We will create three different classes,
one for students, one for teaching staff, and one for accounting officers and others. The separation of the class is based on attributes
because a teacher’s attributes are different from students, and both have different attributes from the members of account officers.
Although many attributes are the same, such as name, age, address, etc. but the teacher also has an attribute salary that the student
does not or an attribute, number of classes that the accounts officers do not possess. So, now we have an understanding of how and on what basis we form
different classes.

Classes are not like function, so we do not have to use the keyword define to create a class; instead, we use the keyword Class along with the name of the
class. Also, we do not call a class as a whole; instead, we use an object to access its different attributes. We can assign new values and can also overwrite
the previous values with the help of an object. In short, an object gives us permission to access the whole class. We can access variables in a class, like:

Object_name.variable_name = “abc”

Here we are setting a variable equal to abc. By doing this its previous value will be overwritten.

Creating Object:
           Creating an object of a class is rather easy and simple. Suppose we have a class named Student. We can create an object of it by these certain
           lines of code:

Stu1 = Student()
Stu2 = Student()
Here we have created two objects of class Student. We can access every item in student using these objects. There is no restriction on the number of objects a
class may have, and also there is no limit to the number of classes a program may have.

An object consists of :
 The State, which is represented by attributes of an object which reflects the properties of an object.
 Methods of an object, which represents the behavior of the object and the response of an object with other objects.
 Identity, which gives a unique name to an object, so that one object can interact with other objects.
"""


class Student:
    pass


Ashish = Student()
Abhijeet = Student()
Amit = Student()

print(Ashish, Abhijeet, Amit)

Ashish.name = "Ashish Giri"
Ashish.standard = 9
Ashish.roll_number = 24
Abhijeet.name = "Abhijeet Singh"
Abhijeet.standard = 9
Abhijeet.roll_number = 32
Amit.name = "Amit Pahurkar"
Amit.standard = 9
Amit.roll_number = 29
