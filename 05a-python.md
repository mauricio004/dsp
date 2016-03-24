# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are ordered sequence of values.   Python identifies each value by an index.  The main difference is that lists are mutable and tuples are inmutable. 
We use tuples as keys in dictionaries as they are inmutable.  

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> A list stores an ordered collection of elements and a set stores an unordered collection of unique elements.
Regarding performance, sets are faster when we want to find an object in a set.  When searching for objects in sets, the speed of this operation does not depend 
on the size of the set like for lists. Lists are faster when we iterate over their content.  
For example, we can have the following list:  
lst = [1, 1, 2, 2, 3]  
Now, we want to create a set from this list:  
st = set(lst)  
The new set contains {1, 2, 3}  
---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> 'lambda' allow us to create small anonymous functions.  These functions are throw-away functions.
For example, assume we have a dictionary with a tuple as key, and we would like to sort by the second element of the tuple.
We can use the following sorted function with lamba in the key argument ->   
sorted(faculty_dict.items(), key=lambda key: key[0][1])


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> A list comprehension allow us to transform a list into another list.
For example:  lst_comp = [2 * x for x in range(5)] creates a new list [0, 2, 4, 6, 8] 
multiplying all elements of the list [0, 1, 2, 3, 4] by 2.  
The equivalent using map: map(lambda x:2*x, range(5)).    
Filter allows us to filter out elements. For example we can filter out even elements from  
the list that range(5) generates.     
filter(lambda x:x%2 == 0, range(5)) - > [0, 2, 4]     
We can use a dictionary comprehensions to populate keys and values in a dictionary.  
d = {n: n * 2 for n in range(5)} --> {0: 0, 1: 2, 2: 4, 3: 6, 4: 18}  
We can also use set comprehensions to populate a set.  
s = {x for x in range(5)} --> {0, 1, 2, 3, 4}  

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

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





