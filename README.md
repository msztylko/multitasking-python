# multitasking-python
sync/async/multithreading/multiprocessing python guide you wish you had found earlier

## Why?
Parallel and concurrent processing in Python is confusig, mainly due to the [Global Interpreter Lock](https://wiki.python.org/moin/GlobalInterpreterLock) and many options to overcome it:  
- [threading](https://docs.python.org/3/library/threading.html)
- [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
- [asyncio](https://docs.python.org/3/library/asyncio.html). 

and more ...

Let's explore differences between these various approaches with a practical example - Broken Link Checker.

## How?

With the broken link checker application written in 4 different ways. The project is organized as follows:  
- multitasking - notebook where I explore various aspects of this project. Check it if you're looking for more explanations
- benchmark.py
- sequential_checker.py
- mulithreading_checker.py
- multiprocessing_checker.py
- asyncio_checker.py
