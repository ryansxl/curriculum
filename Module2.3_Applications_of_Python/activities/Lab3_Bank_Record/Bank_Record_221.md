<!--title={Printing all entries explained}-->

<!--badges={Python:21}-->

<!--concepts={Dictionaries.mdx, Lists.mdx, ForLoops.mdx, IndexingDictionaries.mdx, IndexingLists.mdx}-->

We can just have one **for loop** to iterate through all the entries in `records`.

```python
for entry in records:
```

The rest of the code is under this **for loop**

```python
    print("Name: " + str(entry))
    print("Amount: " + str(records[entry][0]))
    print("memo: " + records[entry][1])
    print("\n")
```

There is a **type difference** here, where `records[entry][0]` returns an **integer**. We cannot concatenate a **string** with an **integer** without converting the **integer** into a **string** first. The same goes for entry. Notice memo is already a **string**.
