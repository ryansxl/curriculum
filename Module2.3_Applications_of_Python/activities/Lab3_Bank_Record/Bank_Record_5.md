<!--title={main()}-->

<!--badges={Python:70}-->

<!--concepts={BooleanOperators.mdx, Lists.mdx, Dictionaries.mdx, UserInput.mdx, IfStatements.mdx, Casting.mdx, WhileLoops.mdx, IndexingDictionaries.mdx}-->

Let's finish writing `main()`. There should be input validation for anything entered besides "0", "1", "2", "3", or "4".

```python
def main():
    ''' Keeps track of a dictionary with key values as:
        {"Name" : [money(int), memos joined (string)]}
        User can choose to print entries, add or remove some, or merge them
    '''
    records = {}

    while (True):
        print_menu()
    
        choice = input("Your choice: ")

        if (choice == 0):
            return

        switch = {
            1: '''TODO''',
            2: '''TODO''',
            3: '''TODO''',
            4: '''TODO'''
        }

        switch[choice](records)
```

