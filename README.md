# 0x00. AirBnB clone - The console
## Description
**First step:** Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

+ put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
+ create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
+ create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
+ create the first abstracted storage engine of the project: File storage.
+ create all unittests to validate all our classes and storage engine  


### What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

+ Create a new object (ex: a new User or a new Place)
+ Retrieve an object from a file, a database etc…
+ Do operations on objects (count, compute stats, etc…)
+ Update attributes of an object
+ Destroy an object
## Notes  
### __str__ and __repr__
The __str__() and __repr__() methods can be helpful in debugging Python code by logging or printing useful information about an object.  

Python special methods begin and end with a double underscore and are informally known as *dunder methods*. Dunder methods are the underlying methods for Python’s built-in operators and functions. You should avoid calling dunder methods directly, and instead implement the dunder methods in your class and then use the built-in functions that call them, such as str() and repr().  
The __repr__() method returns a more information-rich, or official, string representation of an object.  
### Python packages

A Python file can be a module but when this file is in a folder, we call this folder - a package.  
File organization is really important in a big project. This means for Python: packages everywhere.  

from *my_math.abs import my_abs* => YES YES YES! now you can use your function like that: my_abs(89)
Wait, does this really work?

NO! something is missing: the magic file __init__.py

Indeed, each folder must contain this file to be considered a package.

This file should be empty except if you want to import all the content of modules by using *.

my_script.py
my_math/
    __init__.py
    abs.py
    functions/
        __init__.py
        add.py
How can I use my function *my_add(a, b)* from the file *add.py* in my_script.py?

    ```python
    from my_math.functions.add import my_add
    ```
Using *import ** is still considered bad practice in production code. In that case, __init__.py shouldn’t be empty but must contain the list of modules to load:  

Relative versus Absolute import
In this example:

my_script.py
my_math/
    __init__.py
    abs.py
    positive.py
positive.py contains one function def is_positive(n) and this function uses my_abs(n). How it’s possible?

By importing: from my_math.abs import my_abs or from abs import my_abs

What the difference?

+ *from abs import my_abs* is using a relative path(since both are in same directory) between your file that imports and the module to import
+ from my_math.abs import my_abs is using an absolute path between the file you execute and the module to import
### uuid — UUID objects according to RFC 4122
This module provides immutable UUID objects (the UUID class) and the functions uuid1(), uuid3(), uuid4(), uuid5() for generating version 1, 3, 4, and 5 UUIDs as specified in RFC 4122.  

If all you want is a unique ID, you should probably call uuid1() or uuid4(). Note that uuid1() may compromise privacy since it creates a UUID containing the computer’s network address. uuid4() creates a random UUID.  

Depending on support from the underlying platform, uuid1() may or may not return a “safe” UUID. A safe UUID is one which is generated using synchronization methods that ensure no two processes can obtain the same UUID. All instances of UUID have an is_safe attribute which relays any information about the UUID’s safety, using this enumeration:
### datetime — Basic date and time types
The datetime module supplies classes for manipulating dates and times.  

Date and time objects may be categorized as “aware” or “naive” depending on whether or not they include timezone information.  

With sufficient knowledge of applicable algorithmic and political time adjustments, such as time zone and daylight saving time information, an aware object can locate itself relative to other aware objects. An aware object represents a specific moment in time that is not open to interpretation.  

While date and time arithmetic is supported, the focus of the implementation is on efficient attribute extraction for output formatting and manipulation.   
## Links 
+ Python packages concept page  
https://intranet.alxswe.com/concepts/66   
+ How To Use *args and **kwargs in Python 3  
https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3   
+ cmd module  
https://docs.python.org/3.8/library/cmd.html  
+ cmd module in depth  
http://pymotw.com/2/cmd/  
+ uuid module  
https://docs.python.org/3.8/library/uuid.html  
+ datetime  
https://docs.python.org/3.8/library/datetime.html  
+ unittest module  
https://docs.python.org/3.8/library/unittest.html#module-unittest  
+ args/kwargs  
https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/  
+ Python test cheatsheet  
https://www.pythonsheets.com/notes/python-tests.html  
+ cmd module wiki page  
https://wiki.python.org/moin/CmdModule  
+ python unittest  
https://realpython.com/python-testing/  
