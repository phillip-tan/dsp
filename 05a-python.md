# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are a sequence of values of any type and can be indexed by integers. The main difference is that tuples are immutable. Since only immutable elements can be used as the keys in a dictionary, only tuples and not lists will work as keys in dictionaries. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are an unordered collection of unique elements, whereas lists are an ordered collection of elements. As an example, lists are best applicable to sort and have order while sets are preferred for speed when order is irrelevant and duplicates are unwanted. In addition, sets use hash tables while lists use indices. As a result, sets are much faster than lists. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> 'lambda' in Python 

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions is a tool that can be used to transform anything iterable into another list. The new list can have elements that have been conditionally included and each element can be transformed as needed.
For example, instead of using a for loop to append a list of odd numbers and multiply each element by three, one could use list comprehension to improve the syntax and speed. 
odds_tripled = [n * 3 for n in numbers if n % 2 == 1] 
As for an equivalent to the list comprehension example, using 'map' and 'filter', one could reference the following example:
odds_tripled = map(lambda n: n * 3, filter(lambda n: n % 2 == 1, numbers))
Between list comprehensions and 'map' (and 'filter'), their difference in speed differs minimally no matter the scenario in which one is deemed quantitatively faster. The main advantage could be argued in favor of list comprehensions because the syntax is more direct.
An example of set comprehension by transforming the following code that takes the first letter in a sequence of words:
first_letter = set()
for w in words:
  first_letter.add(w[0])
Transform using set comprehension:
first_letter = {w[0] for w in words}
An example of dictionary comprehension by transforming the following code that swaps the keys and values from an original:
flip = {}
for key, value in original.items():
  flip[value] = key
Transform using dictionary comprehension:
flip = {value: key for key, value in original.items()}

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





