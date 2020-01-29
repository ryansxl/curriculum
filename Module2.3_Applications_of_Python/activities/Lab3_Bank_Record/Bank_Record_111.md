<!--title={Printing the menu explained}-->

<!--badges={Python:42}-->

<!--concepts={PrintStatements.mdx, UserInput.mdx, Lists.mdx, ForLoops.mdx}-->

`print_menu()` will need a **list** to iterate through called `options`. Each line of the menu from the example is its own element.

```python
options = [
    'Exit',
    'Print all entries',
    'Add a new entry',
    'Delete an entry',
    'Merge entries'
]
print("Please pick 1-" + str(len(options)))
```

For "Please pick 1-5", we could just type the 5 in, but `str(len(options))` allows us to incorporate more options in the future if we need it. If we added another option, we would not have to change that 5 to a 6.

Then, we have a **for loop** to iterate through the list, and print out all of `option`'s elements. The rest is a matter of formatting to match the prompt. We have to print out integers as type **string,** and we can **type cast** to do so.

```python
# print the options
i = 0
for option in options:
    print(str(i) + ". ", end="")
    print(option, end="\n")
    i += 1
```

