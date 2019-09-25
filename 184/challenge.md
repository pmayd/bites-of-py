# Bite 184. Analyze some Bite stats data

In this Bite we will look at some Bite stats logs (usernames have been anonymized!):

```
$ head -5 bite_output_log.txt
bite,user,completed
102,ofancourt1,False
101,ofancourt1,False
29,emilham4,False
9,mfilshin6,False
````

Load in the data using csv's awesome DictReader storing the result in self.rows in the constructor (__init__). Next finish the 6 defined @property methods using the loaded in data. Each property returns a single value. Check out the docstrings and tests for more info.

Good luck and keep calm and code in Python!
