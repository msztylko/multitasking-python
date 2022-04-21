# multitasking-python

<p align="center">
sync/async/multithreading/multiprocessing in Python   
</p>
<p align="center"> 
<img src="https://github.com/msztylko/multitasking-python/blob/master/images/benchmark.png" data-canonical- width="400" height="600" align="center" />
</p>

## Why?
Parallel and concurrent processing in Python is confusig, mainly due to the [Global Interpreter Lock](https://wiki.python.org/moin/GlobalInterpreterLock) and many options to overcome it:  
- [threading](https://docs.python.org/3/library/threading.html)
- [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
- [asyncio](https://docs.python.org/3/library/asyncio.html)

and more ...

Let's explore differences between these various approaches with a practical example - Broken Link Checker.

## How?

With the broken link checker application written in 4 different ways. The project is organized as follows:  
- [multitasking](./multitasking.ipynb) - notebook where I explore various aspects of this project. Check it if you're looking for more explanations
  - [multiprocessing_check.py](./multiprocessing_check.py) - needed to explore multiprocessing in Jupyter Notebook
- [benchmark.py](./benchmark.py) - main performance comparison of various approaches
- [sequential_checker.py](./sequential_checker.py)
- [multithreading_checker.py](./multithreading_checker.py)
- [multiprocessing_checker.py](./multiprocessing_checker.py)
- [asyncio_checker.py](./asyncio_checker.py)
