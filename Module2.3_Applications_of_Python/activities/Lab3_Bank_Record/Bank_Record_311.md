<!--title={Deleting an entry explained}-->

<!--badges={Python:42}-->

<!--concepts={BooleanOperators.mdx, Lists.mdx, Dictionaries.mdx, UserInput.mdx, IfStatements.mdx}-->

We need to first gather user input to determine which key for which entry to delete.

```python
entryToDel = input("Enter a name: ")
```

Then, we use an **if statement** to remove that entry in `records`. We can use the boolean operator `not` to see if an entry exists. We do not want to try deleting an entry that does not exist or else we will get an error, so we return.

```python
# check if entry exists
if (entryToDel not in records):
    print(entryToDel + " does not exist")
    return
```

Otherwise, we delete the entry using `del`.

```python
# delete the entry
del records[entryToDel]
```

