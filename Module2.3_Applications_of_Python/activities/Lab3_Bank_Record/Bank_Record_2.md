<!--title={insert() and print_all()}-->

<!--badges={Python:70}-->

<!--concepts={Casting.mdx, ForLoops.mdx, UserInput.mdx, IfStatements.mdx, BooleanOperators.mdx, Dictionaries.mdx, IndexingDictionaries.mdx, IndexingLists.mdx, Casting.mdx} -->

Let's write the function `insert()` and `print_all()`.  Have input validation for `insert()` that checks whether the balance is a numerical amount. Do this immediately after the user input for balance is obtained, and before the user input for memo is obtained.

```python
def insert(records):
    ''' inserts a new entry 

		Input: dictionary
		Output: the dictionary now has 1 new element
	'''

def print_all(records):
    ''' print all entries by a given topic
    
    	Prints all entries like so:
    	Name: Joe
    	Amount: 20
    	Comment: Tuesday
    	
    	Input: dictionary
    	Output: prints all entries of records, dictionary unmodified
    '''
    
```

Example output for input validation:

Attempt to create entry with owner as "45" and balance amount of "Joe". The program should not create this entry and instead print a message to let the user know that the input is invalid.

```python
>>> main()
Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 2
Owner: 45
$Joe
Invalid amount: $Joe
Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 1
Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 
```

