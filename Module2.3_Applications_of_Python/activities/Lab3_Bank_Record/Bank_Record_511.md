<!--title={Writing main explained}-->

<!--badges={Python:42}-->

<!--concepts={BooleanOperators.mdx, Lists.mdx, Dictionaries.mdx, UserInput.mdx, IfStatements.mdx, Casting.mdx, WhileLoops.mdx, IndexingDictionaries.mdx}-->

The entirety of `main()` is in a single **while loop**, so all the code below is within

```python
while (True):
```

`records` is a **dictionary**, so initialize it as an empty one, so we can read data into it.

```python
records = {}
```

Now we have to get the user's input, as a number by casting to an **integer**.

```python
choice = int(input("Your choice: "))
```

But wait! If the user enters in a letter, then the program will throw an error, so we have to check for a number input first.

```python
choice = input("Your choice: ")
if (choice.isdigit()
```

Using **short circuiting**, we can add numerical checks to this same **if** condition to see if `choice` is within 0 and 4.

```python
choice = input("Your choice: ")
if (choice.isdigit() and int(choice) >= 0 and int(choice) <= 4):
    choice = int(choice)
```

If this condition doesn't return `True`, then we want to print a message out and start the loop over with **continue**

```python
choice = input("Your choice: ")
if (choice.isdigit() and int(choice) >= 0 and int(choice) <= 4):
    choice = int(choice)
else:
    print("Invalid choice")
    continue 
```

When the user enters 0, the program should stop

```python
if (choice == 0):
    return
```

`switch` should have values that are **function calls**. For example, assume `choice` is 1. Then, the last line `switch[choice](records)` will evaluate `print_all(records)`, which is a **function call**.

```python
switch = {
   1: print_all,
   2: insert,
   3: delete,
   4: merge
}

switch[choice](records)
```

