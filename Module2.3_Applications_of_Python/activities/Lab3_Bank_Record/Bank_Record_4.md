<!--title={Merging entries}-->

<!--badges={Python:170}-->

<!--concepts={UserInput.mdx, IfStatements.mdx, BooleanOperators.mdx, PrintStatements.mdx, Dictionaries.mdx, IndexingDictionaries.mdx, IndexingLists.mdx, Lists.mdx}-->

Ok, for now we will write the function `merge()`. We can use `insert()` to add two entries and `print_all()` to confirm the entries are merged. There should also be input validation immediately after each user input to check whether

* both entries are able to merge
* new entry to merge to doesn't already exist

```python
def merge(records):
    ''' merges two entries into one
        the amounts are added together
        
        1. Asks user for two entries
    	2. Creates new entry with sum amount
    	3. Remove old two
    	
    	Input: dictionary
    	Output: Modifies dictionary
    '''
```

Here is an example output of inserting two entries `"Owner1" : [100, "Memo1"]` and `"Owner2" : [150, "Memo2"]`, then merging them under a new entry with key "NewOwner", and finally printing all entries to show only the merged entry:

```
>>> main()
Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 2
Owner: Owner1
$100
Memo: Memo1
Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 2
Owner: Owner2
$250
Memo: Memo2
Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 4
First entry to merge: Owner1
Second entry to merge: Owner2
Owner of merged entry: NewOwner
Memo: NewMemo
Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 1
Name: NewOwner
Amount: 350
memo: NewMemo


Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 
```

Input Validation Example Outputs:

There are two entries to merge in this example: Ji and JO.

First, we test that the first the entry to merge "f" does not exist.

Then, we test that the second entry to merge "Joe" does not exist.

Lastly, we test that the merged entry (the new entry being created) "Ji" cannot be created because an entry under the name "Ji" already exists.

```
>>> main()
Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 2
Owner: JO
$1
Memo: 2
Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 2
Owner: Ji
$2
Memo: f
Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 4
First entry to merge: f
f not found
Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 4
First entry to merge: Ji
Second entry to merge: Joe
Joe not found
Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 4
First entry to merge: Ji
Second entry to merge: JO
Owner of merged entry: Ji
Ji already exists
Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 
```

