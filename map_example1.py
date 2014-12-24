#!/usr/bin/env python

"""
 with map() we can work applying a function to the items of a list or lists
 in this example we will using lambda to define mini functions
"""

items = [1,2,3,4,5,6,7,]
result = map(lambda x : x**2, items)

print 'items before apply lambda function'
print items
print 'lambda funtion defines a x^2'
print 'result list after apply lambda function'
print result

