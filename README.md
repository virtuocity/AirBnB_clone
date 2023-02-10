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
