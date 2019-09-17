# Bite 48. Make a bar chart of new Safari books

Some time ago we made a little Slack bot to post new titles added to Safari to Slack. And luckily we added logging so we have some data for you to play with :)

In this Bite you will make a small bar chart of the amount of books it sent every day in February. To limit the data we just look at 10 days worth of data.

The log is loaded into the template code and has this format:
```
02-13 01:59 root         DEBUG    9781788838542  [Titel anhand dieser ISBN in Citavi-Projekt übernehmen]  - WinOps - DevOps on the Microsoft Azure Stack: VSTS and TFS 2018
02-13 01:59 root         DEBUG    - sending to slack channel
02-13 01:59 root         DEBUG    9781787285217  [Titel anhand dieser ISBN in Citavi-Projekt übernehmen]  - Python Web Scraping Cookbook
02-13 01:59 root         DEBUG    - cached, skipping
...
02-13 04:59 root         DEBUG    9781788838115  [Titel anhand dieser ISBN in Citavi-Projekt übernehmen]  - JIRA Administration - Getting Started with JIRA
02-13 04:59 root         DEBUG    - cached, skipping
02-13 05:59 root         DEBUG    9780134858968  [Titel anhand dieser ISBN in Citavi-Projekt übernehmen]  - My Windows 10 (includes video and Content Update Program)
02-13 05:59 root         DEBUG    - sending to slack channel
02-13 05:59 root         DEBUG    9781788838542  [Titel anhand dieser ISBN in Citavi-Projekt übernehmen]  - WinOps - DevOps on the Microsoft Azure Stack: VSTS and TFS 2018
02-13 05:59 root         DEBUG    - cached, skipping
...
```

You need to count the sending to slack channel entries and look at the book title in the previous line (yes we like to challenge you!) - and see if it was a Python book. If so print 🐍 , else a dot (constants provided).

Here is the output you need to achieve. No need to return, just print it, our pytest code just calls your function and checks the stdout it returns.
```
02-13 ...........
02-14 ..............
02-15 .................
02-16 ............
02-19 🐍.......🐍
02-20 ...
02-21 ..............🐍
02-22 🐍...................
```