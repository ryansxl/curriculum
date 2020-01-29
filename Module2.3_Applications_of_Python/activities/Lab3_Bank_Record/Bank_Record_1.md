<!--title={Bank Record}-->
<!--badges={Python:70}-->

<!--concepts={PrintStatements.mdx, UserInput.mdx, Lists.mdx, ForLoops.mdx}-->

![pink pig figurine on white surface](https://images.unsplash.com/photo-1459257831348-f0cdd359235f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=80)

Let's write a simple, user-friendly database for storing a bank. This program uses a dictionary to keep track of each entry. The keys will be a **string** of the owner of the account, and the values will be a **list** of attributes for that entry. The list will have two elements, the first being an **integer** of that entry's amount of money, and the second element will be a **string** that represents a comment to go with that entry **in that order**! An example looks like this:

`"Joe" : [5000, "Created on January 1, 1998"]`

For simplicity, you can assume valid input for most of the functions.

There will be five functions to write: `delete()`, `insert()`, `merge()`, `print_all()`, `print_menu()`.

Here is how `print_menu()`  should look:

```
>>> main()
Please pick 1-5
0. Exit
1. Print all entries
2. Add a new entry
3. Delete an entry
4. Merge entries
Your choice: 
```

Now let's write the `print_menu()` function.

```python
def print_menu():
    ''' prints available options 
    	Input: none
    	Output: prints the list of options'''
    # a list of all available options
```

Here is example output of inserting two entries `"Owner1" : [100, "Memo1"]` and `"Owner2" : [150, "Memo2"]`, then merging them under a new entry with key "NewOwner", then finally printing all entries to show only the merged entry:

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

