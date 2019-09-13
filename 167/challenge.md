# Bite 167. Complete a User class: properties and representation dunder methods

In this Bite you are presented with another class, User this time.

Like last Bite you are asked to complete it, see the TODOs in the code below:

- Complete the `get_full_name property` (more on properties here) that prints first and last name separated by a space.
- Complete the `username` property following its docstring.
- Complete the special representation dunder methods: `__str__`` and __repr__`. Look at the tests what they should return. Brace yourself for some bonus learning for a twist we added in `__repr__` (but as it's a Beginner Bite we give you a hint!)

Apart from Ned's awesome answer on SO, to give you an idea about the difference between `__str__` and `__repr__`, check out how datetime implements them:

```python
>>> from datetime import datetime
>>> dt = datetime.now()
>>> str(dt)
'2019-02-04 23:05:27.376407'
>>> repr(dt)
'datetime.datetime(2019, 2, 4, 23, 5, 27, 376407)'
```

Good luck and keep calm and code in Python!
