#!/usr/bin/python

#from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool as ThreadPool

urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://toly.github.io/blog/2014/02/13/parallelism-in-one-line/',
    'https://docs.python.org/2/library/multiprocessing.html'
    ]

def printurl( url ):
    return url

pool = ThreadPool(4)

results = pool.map(printurl, urls)
print results

pool.close()
pool.join()

