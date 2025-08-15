""" 
Generators are a special type of iterator in Python, designed to yield values one at a time, allowing for efficient
memory usage and lazy evaluation. They provide a convenient way to implement iterators using the yield keyword, avoiding 
the complexity of writing a class-based iterator.
"""



#generator function
def firstn(n: int):
    num: int = 0
    while num < n:
        yield num
        num += 1


# generator expression
squares = (x * x for x in range(10))

