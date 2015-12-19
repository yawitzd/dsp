# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> 
  1. Order! 
        Lists are ordered
        Tuples are unordered
  2. Structure
        Lists are ordered, but every value means the same thing.
            hours = [12.00, 1.00, 2,00, 3.00, 4.00]
        Tuples are unordered, but values have semantic meaning. 
            datetime.tuple = ["Jan", 13, 2016, 2, 45]
  3. Editing
        Tuples are immutable. Once tuple values have been created, they cannot be edited or replaced.
        Lists can be changed.
        Both lists and tuples can be sliced, edited, concatenated. 
        Since tuples are immutable they CAN be used as dictionary keys.
  4. Size
        A tuple is slightly fewer bits than a list. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> 
 A set is an unordered collection with no duplicates (e.g. a set of user IDs)
  set('abracadabra') #gives the unique letters in that string
 A list is an ordered collection that can contain duplicated (e.g. days of the week in August)
  list('abracadabra') #gives the letters in that string, in order

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> 
Lambda is a shorthand for creating functions. Eg:
  name = lambda sorted: key

Is the same as:
  def name(sorted):
      return key

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are lists that are exported from functions. For example, this function returns a list of the first 10 square numbers:
def sqlist():
    sqs = []
    for i in range(10):
        sqs.append((i+1)**2)
    return sqs
    
"Map" is another way to export a list comprehension. "Map" is a processing pattern that traverses a sequence and performs an operation on each element. For example, this funcion takes a string and capitalizes every letter:

def capitalize_all(t):
    '''from Dowley, p91'''
    res = []
    for s in t:
        res.append(s.capitalize())
    return s
    
"Filter" can also give list comprehensions; "filter" takes some elements sequence and exports a list of those elements. For example, this function exports a list of all the vowels in the string, in order. 

def vowel_list(t)
  vowels = ['a','e','i','o','u']
  v = []
  for s in t:
      if s in vowels:
          v.append(s)
  return v

Sets are unordered collections of unique elemetns. We can also run set comprehensions to collect sets of values from sequences. Sets are enclosed in curly braces: {} and we can operate on them using these functions: https://docs.python.org/2/library/sets.html . For example, this takes two sets (girls and boys), then exports their union, 'supergroup'
girls = {'Michelle', 'Kelly', 'Beyonce'}
boys = {'Justin', 'Lance', 'Joey'}

Dictionary comprehensions export dictionaries of chosen elements from a sequence. 

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





