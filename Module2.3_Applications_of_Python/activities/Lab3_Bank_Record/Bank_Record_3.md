<!--title={Deleting an entry}-->

<!--badges={Python:70}-->

<!--concepts={BooleanOperators.mdx, Lists.mdx, Dictionaries.mdx, UserInput.mdx, IfStatements.mdx}-->

Now we need to write the function `delete()`.

```python
def delete(records):
    ''' removes an entry from records 
    	1. Asks user for key (entry's owner's name)
    	2. Check if entry exists
    	3. Deletes the entry
    	
    	Input: dictionary
    	Output: modifies dictionary
    '''
```

Here is example output of inserting an entry `"Bob" : [10, "Nothing"]`, then printing all entries (in this case, just that one) out, then deleting it, and finally printing out all entries to show there are none:

```
>>> main()
Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 2
Owner: Bob
$10
Memo: Nothing
Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 1
Name: Bob
Amount: 10
memo: Nothing


Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 3
Enter a name: Bob
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
