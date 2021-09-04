Welcome to my IT FDN 100 page!
<br>See the markdown on [index.md](https://github.com/rblake50/IntroToProg-Python/blob/main/docs/index.md)
# Homework Links
|Homework|Link|Uploaded|
|---|---|---|
|HW08|[Link to HW08 files](https://github.com/rblake50/IntroToProg-Python/tree/main/HW08)|TBD|
|HW07|[Link to HW07 files](https://github.com/rblake50/IntroToProg-Python/tree/main/HW07)|08/23/2021|
|HW06|[Link to HW06 files](https://github.com/rblake50/IntroToProg-Python/tree/main/HW06)|08/15/2021|
|HW05|*Need to link*|To do|
|HW04|*Need to link*|To do|
|HW03|*Need to link*|To do|
|HW02|*Need to link*|To do|
|HW01|*Need to link*|To do|
***
# Module08 Learnings
Constructors are useful for initiating new objects.
```python
class Product:
  def __init__(self,param1,param2):
    print("You created a new Product object!")
    self.name = param1
    self.price = param2

  def __str__(self):
    str = "The " + self.name + " Product has a price of " + self.price
    return str
```

# Module07 Learnings
## Pickling
At this point in the course, we have learned how to perform basic operations with Python and deal with data collections like tuples, lists, and dictionaries within the Python development environment and simple text files. While this approach offers near-infinite possibilities for user design and data saving, there is a more effective way to save objects with information compared to simple text files. The technique is known as “pickling.”

The textbook provides an excellent definition, copied here for reference: “Pickling means to preserve—and that’s just what it means in Python. You can pickle a complex piece of data, like a list or dictionary, and save it in its entirety to a file. Best of all, your hands won’t smell like vinegar when you’re done.” The technique can avoid some common hassles related to simple text interpretation such as if delimiting or formatting conventions change throughout a document.

The following online resources were found to be helpful:

* [Pickle in Python: Object Serialization](https://www.datacamp.com/community/tutorials/pickle-python-tutorial)
* [What is Pickling in Python?](https://www.afternerd.com/blog/python-pickle/)

All pickling requires the pickle library to be imported.
```python
import pickle
```
Data can be read using `load()`.
```python
# Deserialize data
with open(strFileToRead,'rb') as f:
  e = pickle.load(f)
```
Data can be written using `dump()`.
```python
# Serialize data (overwite)
with open(strFileToSave,'wb') as file:
  pickle.dump(someData,file)
```
***
## Error Handling
Error handling is another valuable function within Python. Basic error handling can be wrapped into a straightforward block of (pseudo)code:

```python
try:
  some_action
except:
	print(“Custom error message”)
else:
	next_action # if there is no error
finally:
  another_action # in success or error case
```
While Python has default error messaging, it is designed for developers and not users. Adding custom error handling can improve user experience and clarify errors, especially regarding user input.

The except block offers a few added tricks for error handling. One involves the interpretation of different error codes.
```python
try:
  some_action
except ValueError:
	print(“You have a value error!”)
except IOError as e:
	print(“You have an IO error!”)
	print(e) # Default Python error message for IOError
else:
	next_action
```
As shown, specific errors can be addressed, and the default error handling can even be captured for controlled usage.
***
# Module06 Website
[Google Homepage](https://www.google.com "Google's Homepage")
<br>[GitHub Webpage Code CheatSheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
