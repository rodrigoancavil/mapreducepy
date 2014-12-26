#!/usr/bin/env python

"""
 example of reduce().
 this takes a list of orders and groups it by for order id (id) and sum per order id
 we used map(), filter() and reduce() to build the example
"""

def myreduce(items):
     result = []
     for key in dict(items).keys():
         elems = filter(lambda x : x[0] == key, items)
         value = reduce(lambda x, y: x+y, map(lambda x : x[1], elems))
         result.append((key, value))
     return result

orders = [
	  {'id' : "apples", 'qty' : 10, 'dest': 'north' },
	  {'id' : "oranges", 'qty' : 15, 'dest': 'south' },
	  {'id' : "apples", 'qty' : 50, 'dest': 'east' },
	  {'id' : "apples", 'qty' : 30, 'dest': 'west' },
	  {'id' : "tomatoes", 'qty' : 130, 'dest': 'west' },
	  {'id' : "oranges", 'qty' : 30, 'dest': 'west' },
         ]

m = map(lambda order : (order['id'],order['qty']), orders)
print myreduce(m)

