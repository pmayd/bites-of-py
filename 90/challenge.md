
# Bite 90. What South Park characters talk most?

Did we already tell you we love the collections module? In this Bite we combine its defaultdict and Counter data structures for powerful data querying.

We will use this cool South Park data set (thanks Peter for the idea and collaboration on this one!). See the template below: we already completed get_season_csv_file to load in the csv data for a given season.

You need to complete get_num_words_spoken_by_character_per_episode which receives the loaded csv data (example) and parse it into a defaultdict of Counter objects. Here is a snippet what you should end up with:

```
                {'Agent 1': Counter({'8': 48, '2': 1}),
...
# Counter k,v here = (episode, # number of words spoken)
...
                'Anthropologist': Counter({'12': 101}),
...
                'Cartman': Counter({'1': 735,
                                    '10': 669,
                                    '13': 621,
... etc ...
```

Why is this cool? This structure makes it easy to do lookups by character, for example: Cartman was most talkative in episode 1, Agent 1 in episode 8, etc. See more checks under the TESTS tab. Ready to add collections to your toolkit? Have fun!

