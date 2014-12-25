#!/usr/bin/env python
"""
 example of reduce()
 this take a list of items and applies a function to return a result
 we will using reduce() with map() to process json
 map() makes a list with quantities only and,
 reduce() sum
"""
items = [{'id' : 'oranges' , 'quantity' : 10},
         {'id' : 'apples' , 'quantity' : 30},
         {'id' : 'tomatoes' , 'quantity' : 56}
        ]

result = reduce(lambda x,y : x + y, map(lambda a : a['quantity'], items))

print result
