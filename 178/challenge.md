# Bite 178. Parse PyBites blog git commit log

In this Bite we want to figure out how active we've been on our blog.

To start our data analysis we ran the following command on our blog repo: `git log --stat | egrep "^Date|file.*changed," |grep -B1 changed|grep -v '\-\-'|sed 'N;s/\n/ |/'` which resulted in the following log which should be easier to work with:

```
Date:   Tue Mar 5 22:34:33 2019 +0100 | 2 files changed, 4 insertions(+), 4 deletions(-)
Date:   Tue Mar 5 20:34:34 2019 +0100 | 1 file changed, 2 insertions(+), 2 deletions(-)
Date:   Tue Mar 5 19:02:56 2019 +0100 | 2 files changed, 31 insertions(+), 2 deletions(-)
Date:   Tue Mar 5 14:18:55 2019 +0100 | 3 files changed, 3 insertions(+), 3 deletions(-)
Date:   Tue Mar 5 14:03:55 2019 +0100 | 2 files changed, 51 insertions(+), 39 deletions(-)
Date:   Tue Mar 5 13:23:51 2019 +0100 | 4 files changed, 109 insertions(+), 94 deletions(-)
...
[930 rows more]
...
```

Complete `get_min_max_amount_of_commits`, parsing this file into a `dict` where keys are year/months (you can use the `YEAR_MONTH` constant), and values are the total number of changes as measured by # insertions + # deletions (number of file changes can be ignored). Return a tuple of (least_active_month, most_active_month).

Your code should work if we call it for a smaller data set as well. So if we pass in the optional `year` arg of 2018, it should give the min and max month only for that year (see also the tests).

By the way, with a min, max of (`'2019-01', '2019-03'`), this year's trend is looking pretty good so far :)

Good luck and keep calm and code in Python!
