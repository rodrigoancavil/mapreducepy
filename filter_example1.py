#!/usr/bin/env python

"""
 example of filter()
 filter() takes the items of a list and applies a function, if a item satisfies with the 
 condition, the item passes to the result list.
"""
items = [{'id':'pencils','quantity':10},
         {'id':'pendrives','quantity':100},
         {'id':'cds','quantity':4},
         {'id':'dvds','quantity':1},
        ]

results = filter(lambda x: x['quantity'] < 10, items)
print 'items before filter()'
print items
print 'lambda function let pass only items with quantity less 10'
print 'results after filter()'
print results
