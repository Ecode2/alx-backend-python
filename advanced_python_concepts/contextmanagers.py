"""
Context managers in Python ensure that resources are properly acquired and released, 
typically using the with statement. This is especially useful for handling file operations, network connections, or locks.
"""

""" Class-based Context Managers: Implemented using __enter__and __exit__ methods.
Context Manager using contextlib: A more succinct way to create context managers using decorators and generator functions. """



class File:
    def __init__(self, filename, method):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


# Context Manager using contextlib:

from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()

with open_file('demo.txt') as f:
    f.write('Hello World!')            