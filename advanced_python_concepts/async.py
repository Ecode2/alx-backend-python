""" 
Coroutines: Functions defined with async def that can be paused and resumed.
** Event Loop**: Manages the execution of coroutines and other asynchronous tasks.
Concurrency with asyncio: Running multiple coroutines concurrently without multithreading.
"""

import asyncio

async def greet(name):
    print(f"Hello {name}")
    await asyncio.sleep(1)
    print(f"Goodbye {name}")

asyncio.run(greet("World"))



# Running Multiple Coroutines:

async def main():
    await asyncio.gather(
        greet("Alice"),
        greet("Bob"),
    )

asyncio.run(main())