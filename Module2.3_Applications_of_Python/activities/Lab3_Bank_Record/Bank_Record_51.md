<!--title={Switch statement}-->

<!--badges={Python:21}-->

<!--concepts={Dictionaries.mdx, IndexingDictionaries.mdx, Casting.mdx, IfStatements.mdx, BooleanOperators.mdx}-->

Remember, **dictionaries** take in a key and return the associated value. In `main()`, the dictionary is returning what? Let's take a look at `switch[choice](records)`. First `switch[choice]` will evaluate to some kind of value of unknown data type, let's call this value `some_value`. Then `some_value` is followed by `(records)`. Altogether, this is `some_value(records)`, what does this look like? What type is `some_value` supposed to be then?

For input validation, we can't just type cast the user input to an **integer**. What if they entered a letter? Use `isdigit()` to check for a numerical input, and check the range entered, too.

