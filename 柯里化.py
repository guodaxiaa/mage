#!/usr/bin/python
#coding:utf-8
import time
import datetime
def logger(fn): #修饰函数,参数是一个函数,结果是返回一个函数
    def wrap(*args,**kwargs): #解构参数,未知参数和已知参数
        #before
        print ('args={},kwargs={}'.format(args,kwargs))
        start=datetime.datetime.now()
        ret=fn(*args,**kwargs)
        #after
        delta=(datetime.datetime.now()-start).total_seconds()
        if delta >2:
            print ("{} took {}s".format(fn.__name__,delta))
        return ret
    return wrap

@logger
def add(x,y):
    time.sleep(3)
    return x + y

print (add(2,5))
