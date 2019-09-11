# Bite 11. Enrich a class with dunder methods

[Link](https://codechalleng.es/bites/11/)

Let's enrich an Account class by adding dunder (aka special) methods to support the following:

- length of the object: `len(acc)` returns the number of transactions
- account comparison: `acc1 >,<,>=.<=,== acc2` returns a boolean comparing account balances
- indexing: `acc[n]` shows the nth transaction onaccount (0 based)
- iteration: `list(acc)` returns a sequence of account transactions
- operator overloading: `acc + int` and `acc - int` can be used to add/subtract money
- string representation: `str(acc)` returns NAME account - balance: INT

The provided template already does some setup for you.

Check out the tests for more specifics. Good luck!
