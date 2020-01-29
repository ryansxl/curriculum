<!--title={Inserting entries explained}-->

<!--badges={Python:21}-->

<!--concepts={PrintStatements.mdx, UserInput.mdx, Lists.mdx, ForLoops.mdx, IfStatements.mdx, BooleanOperators.mdx, Casting.mdx}-->

We first gather data from the user about the owner, balance amount, and memo.

```python
name = input("Owner: ")
money = int(input("$"))
memo = input("Memo: ")
```

Note the type difference in `money`. All user input is interpreted as a string, but we want an integer. However, if the user input a letter like "a" or a non-numerical value like "Jim" for `money`, then trying to cast "Jim" into an **integer** will throw an error.

Let's check for this using `isdigit()` before we cast to an **integer**.

```python
name = input("Owner: ")
money = int(input("$"))
if (not money.isdigit()):
    print("Invalid amount: $" + money)
    return
memo = input("Memo: ")
```



Then, we create the new entry `[money, memo]` and assign it to `records` using the key `name` and square brackets [].

```python
# create the entry and assign it to using appropriate key
records[name] = [money, memo]
```
