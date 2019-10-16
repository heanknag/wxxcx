#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sort_locks.py
# @Author: hak
# @Date  : 2019-05-16
# @Desc  :
import threading
from contextlib import contextmanager

# Thread-local state to stored information on locks already acquired
_local = threading.local()

@contextmanager
def acquire(*locks):
    # 按对象标识符对锁排序
    locks = sorted(locks, key=lambda x: id(x))


    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # 按采集的相反顺序释放锁
        for lock in reversed(locks):
            lock.release()


x_lock = threading.Lock()
y_lock = threading.Lock()

def thread_1():
    while True:
        with acquire(x_lock, y_lock):
            print('Thread-1')

def thread_2():
    while True:
        with acquire(y_lock, x_lock):
            print('Thread-2')


t1 = threading.Thread(target=thread_1)
t1.start()
t2 = threading.Thread(target=thread_2)
t2.start()