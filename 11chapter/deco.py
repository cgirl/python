#!/usr/bin/env python
#coding:gbk

from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s called' % (ctime(), func.__name__)
        func()
        return func
    print 'the func is tsfunc'
    return wrappedFunc

print '----------------------'  #ֱ������
@tsfunc                         #���У�����wrappedFunc����funcҲ����foo������,����װΪ��wrappedFunc
def foo():
    print 'the func is foo'

print '*********************'   #ֱ������

foo()                           #ʵ����������wrappedFunc
sleep(4)

for i in range(2):
    sleep(1)
    foo()
