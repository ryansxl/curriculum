<!--title={Merging entries}-->

<!--badges{Python:102}-->

<!--concepts={BooleanOperators.mdx, Lists.mdx, Dictionaries.mdx, UserInput.mdx, IfStatements.mdx} -->

We first gather user input for data to determine which two entries the user wants to merge as well as the key (owner name) of the new entry to be created and its memo.

```python
entry1 = input("First entry to merge: ")
entry2 = input("Second entry to merge: ")
mergedEntry = input("Owner of merged entry: ")
memos = input("Memo: ")
```

We have to validate all the inputs except `memos` because moving on.

We should do this immediately after each `input()` call, not at the end of all for of them.

For `entry1` and `entry2`, check whether they already exist.

```python
entry1 = input("First entry to merge: ")
if (entry1 not in records):
    print(entry1 + " not found")
    return

entry2 = input("Second entry to merge: ")
if (entry2 not in records):
    print(entry2 + " not found")
    return
```

For `mergedEntry`, check the opposite (that it doesn't exist).

```python
mergedEntry = input("Owner of merged entry: ")
if (mergedEntry in records):
    print(mergedEntry + " already exists")
    return
memos = input("Memo: ")
```

The entire code block now looks like:

```python
entry1 = input("First entry to merge: ")
if (entry1 not in records):
    print(entry1 + " not found")
    return

entry2 = input("Second entry to merge: ")
if (entry2 not in records):
    print(entry2 + " not found")
    return

mergedEntry = input("Owner of merged entry: ")
if (mergedEntry in records):
    print(mergedEntry + " already exists")
    return
memos = input("Memo: ")
```

Before we delete anything, we need to preserve the money amounts of both entries to-be-merged. We store this in `total`. We index records essentially by indexing a **list** within a **dictionary**.

```python
# get the total money and remove individual entries
total = records[entry1][0] + records[entry2][0]
```

Then, we can delete the two entries.

```python
del records[entry1]
del records[entry2]
```

Finally, we can use all the data we saved `total`, `memos` and `mergedEntry` and insert that into `records`.

```python
# create new merged entry
records[mergedEntry] = [total, memos]
```
